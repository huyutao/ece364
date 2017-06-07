import numpy as np
from scipy import ndimage
#import pillow
import zlib
import base64
import re
import random
import time

class Payload:
    def __init__(self, img=None, compressionLevel=-1, content=None):
        if img is not None:
            if compressionLevel < -1 or compressionLevel > 9:
                raise ValueError("compressionLevel should in range -1 to 9")
            if type(img) is not np.ndarray:
                raise TypeError("image is not ndarray")
            self.img = img
            comp_data = self.compress_img(compressionLevel)
            xml_pack = self.generate_xml(comp_data,compressionLevel)
            self.convert_base64(xml_pack)

        elif content is not None:
            if type(content) is not np.ndarray:
                raise TypeError("content is not nparray")
            self.content = content
            xml_pack = self.convert_content()
            self.release_xml(xml_pack)
        else:
            raise ValueError("no image or content provided")

    def compress_img(self,compressionLevel):
        flat_arr = self.raster_scan()
        if compressionLevel == -1:
            return flat_arr
        else:
            np_compressed_bytes = zlib.compress(flat_arr,compressionLevel)
            np_compressed_array = np.frombuffer(np_compressed_bytes,dtype=np.uint8)
            return np_compressed_array

    def raster_scan(self):
        size_of_np = list(self.img.shape)
        if len(size_of_np) == 2:
            return self.img.flatten()
        else:
            r_layer = self.img[:, :, 0].flatten()
            b_layer = self.img[:, :, 1].flatten()
            g_layer = self.img[:, :, 2].flatten()
            return np.concatenate((r_layer, b_layer, g_layer))

    def decompress_img(self,compressed_data):
        np_compressed_bytes = compressed_data.tobytes()
        np_decompressed_bytes = zlib.decompress(np_compressed_bytes)
        flat_arr = np.frombuffer(np_decompressed_bytes,dtype=np.uint8)
        return flat_arr

    def generate_xml(self,comp_data,compressionLevel):
        if compressionLevel == -1:
            if_comp = "False"
        else:
            if_comp = "True"
        size_of_np = list(self.img.shape)
        if len(size_of_np) == 2:
            color = "Gray"
            row, col = self.img.shape
        else:
            color = "Color"
            row, col, _ = self.img.shape

        result = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><payload type=\"{}\" size=\"{},{}\" compressed=\"{}\">".format(color,row,col,if_comp)
        content = ",".join(comp_data.astype('str'))
        result += content + "</payload>"
        return result


    def release_xml(self,xml_pack):
        pattern = b"<\?xml version=\"1.0\" encoding=\"UTF-8\"\?><payload type=\"(?P<color>Color|Gray)\" size=\"(?P<size>[\d]+,[\d]+)\" compressed=\"(?P<if_comp>True|False)\">(?P<content>[,\d]+)</payload>"
        m = re.match(pattern,xml_pack)
        color = m.group("color").decode("utf-8")
        size = m.group("size").decode("utf-8")
        if_comp = m.group("if_comp").decode("utf-8")
        content = m.group("content").decode("utf-8")
        row = int(size.split(",")[0])
        col = int(size.split(",")[1])
        if color == "Color":
            hight = 3
        else:
            hight = 1
        comp_data = np.array(list(map(int,content.split(","))),dtype=np.uint8)  #0.6571s
        #comp_data = np.array(content.split(",")).astype(np.uint8)                #1.0691s
        if if_comp == "True":
            comp_data = self.decompress_img(comp_data)
        self.generate_img(comp_data,row,col,hight)

    def generate_img(self,comp_data,row,col,hight):
        if hight == 1:
            self.img = comp_data.reshape(row,col)
        else:
            r_layer, b_layer, g_layer = np.split(comp_data,3)
            r_layer = r_layer.reshape(row,col)
            b_layer = b_layer.reshape(row, col)
            g_layer = g_layer.reshape(row, col)
            self.img = np.dstack((r_layer,b_layer,g_layer))


    def convert_base64(self,xml_pack):
        encode_xml = base64.b64encode(bytes(xml_pack,"utf-8"))#.decode("utf-8")
        if encode_xml[-1:] == "=".encode("utf-8"):   # remove padding
            encode_xml = encode_xml[:-1]
        if encode_xml[-1:] == "=".encode("utf-8"):   # remove padding
            encode_xml = encode_xml[:-1]
        xml_np_arr = np.frombuffer(encode_xml,dtype=np.uint8)
        self.content = xml_np_arr.copy()
        self.content[np.logical_and(48 <= xml_np_arr, xml_np_arr <= 57)] += 4
        self.content[np.logical_and(65 <= xml_np_arr, xml_np_arr <= 90)] -= 65
        self.content[np.logical_and(97 <= xml_np_arr, xml_np_arr <= 122)] -= 71
        self.content[xml_np_arr == 43] = 62
        self.content[xml_np_arr == 47] = 63



    def convert_content(self):
        # vfunc = np.vectorize(int6bit_to_b64str,otypes=[np.uint8])
        # xml_np_arr = vfunc(self.content)
        xml_np_arr = self.content.copy()
        xml_np_arr[self.content <= 25] += 65
        xml_np_arr[np.logical_and(26 <= self.content, self.content <= 51)] += 71
        xml_np_arr[np.logical_and(52 <= self.content, self.content <= 61)] -= 4
        xml_np_arr[self.content == 62] = 43
        xml_np_arr[self.content == 63] = 47
        encode_xml = xml_np_arr.tobytes()
        missing_padding = len(encode_xml) % 4     # add padding
        if missing_padding != 0:
            encode_xml += b'=' * (4 - missing_padding)
        xml_pack = base64.b64decode(encode_xml)
        return xml_pack


class Carrier:
    def __init__(self, img):
        if img is not None:
            if type(img) is not np.ndarray:
                raise TypeError("image is not ndarray")
            self.img = img
            size_of_np = list(self.img.shape)
            if len(size_of_np) == 2:
                self.color = 2
                self.row, self.col = self.img.shape
            else:
                self.color = 3
                self.row, self.col, _ = self.img.shape


    def extract_rgb(self,new_img):
        size_of_np = list(self.img.shape)
        if len(size_of_np) == 2:
            r_layer = new_img.reshape(int(new_img.size / 3), 3)[:, 0]
            g_layer = new_img.reshape(int(new_img.size / 3), 3)[:, 1]
            b_layer = new_img.reshape(int(new_img.size / 3), 3)[:, 2]
        else:
            r_layer = new_img[:, :, 0].reshape(new_img[:, :, 0].size)
            g_layer = new_img[:, :, 1].reshape(new_img[:, :, 1].size)
            b_layer = new_img[:, :, 2].reshape(new_img[:, :, 2].size)
        return r_layer,g_layer,b_layer

    def payloadExists(self):
        xml_start = np.array([15, 3, 61, 56, 27, 22, 48, 32, 29, 38, 21, 50, 28, 54, 37, 47, 27, 35, 52, 34, 12, 18, 56, 48, 8, 34, 1, 37, 27, 38, 13, 47, 25, 6, 37, 46, 25, 51, 52, 34, 21, 21, 17, 6, 11, 19, 32, 34, 15, 51])
        new_img = np.copy(self.img)
        r_layer,g_layer,b_layer = self.extract_rgb(new_img)
        ext_from_r = np.bitwise_and(r_layer[:50], 3)
        ext_from_g = np.bitwise_and(g_layer[:50], 3)
        ext_from_b = np.bitwise_and(b_layer[:50], 3)
        ext_all = np.bitwise_or(np.bitwise_or(np.left_shift(ext_from_b, 4), np.left_shift(ext_from_g, 2)), ext_from_r)
        return np.array_equal(ext_all,xml_start)


    def clean(self):
        random_size = self.img[:, :, 0].size
        random_num = np.random.randint(66,size=random_size)
        new_img = np.copy(self.img)
        r_layer, g_layer, b_layer = self.extract_rgb(new_img)
        emb_to_r = np.bitwise_and(random_num, 3)
        emb_to_g = np.right_shift(np.bitwise_and(random_num, 12), 2)
        emb_to_b = np.right_shift(np.bitwise_and(random_num, 48), 4)
        r_layer[:emb_to_r.size] = np.bitwise_or(np.bitwise_and(r_layer[:emb_to_r.size], 252), emb_to_r)
        g_layer[:emb_to_g.size] = np.bitwise_or(np.bitwise_and(g_layer[:emb_to_g.size], 252), emb_to_g)
        b_layer[:emb_to_b.size] = np.bitwise_or(np.bitwise_and(b_layer[:emb_to_b.size], 252), emb_to_b)
        return new_img

    def embedPayload(self, payload, override=False):
        if type(payload) is not Payload:
            raise TypeError("payload is not Payload type")
        elif payload.content.size * 3 > self.img.size:
            raise ValueError("payload size is larger than what the carrier can hold")
        elif override == False and self.payloadExists():
            raise Exception("current carrier already contains a payload")
        else:
            new_img = np.copy(self.img)
            r_layer, g_layer, b_layer = self.extract_rgb(new_img)
            emb_to_r = np.bitwise_and(payload.content, 3)
            emb_to_g = np.right_shift(np.bitwise_and(payload.content, 12), 2)
            emb_to_b = np.right_shift(payload.content, 4)
            r_layer[:emb_to_r.size] = np.bitwise_or(np.bitwise_and(r_layer[:emb_to_r.size], 252),emb_to_r)
            g_layer[:emb_to_g.size] = np.bitwise_or(np.bitwise_and(g_layer[:emb_to_g.size], 252), emb_to_g)
            b_layer[:emb_to_b.size] = np.bitwise_or(np.bitwise_and(b_layer[:emb_to_b.size], 252), emb_to_b)
            return new_img

    def extractPayload(self):
        new_img = np.copy(self.img)
        r_layer, g_layer, b_layer = self.extract_rgb(new_img)
        ext_from_r = np.bitwise_and(r_layer, 3)
        ext_from_g = np.bitwise_and(g_layer, 3)
        ext_from_b = np.bitwise_and(b_layer, 3)
        ext_all = np.bitwise_or(np.bitwise_or(np.left_shift(ext_from_b,4),np.left_shift(ext_from_g,2)),ext_from_r)
        return Payload(content=ext_all)


    def embedPayloadAdvanced(self, payload, initialPoint, step):
        new_img = np.copy(self.img)
        size_of_np = list(self.img.shape)
        row_x, col_y = initialPoint
        initialPoint_index = row_x * self.col + col_y
        if len(size_of_np) == 2:
            r_layer = new_img.reshape(int(new_img.size / 3), 3)[:, 0]
            g_layer = new_img.reshape(int(new_img.size / 3), 3)[:, 1]
            b_layer = new_img.reshape(int(new_img.size / 3), 3)[:, 2]
        else:
            r_layer = new_img[:, :, 0].reshape(new_img[:, :, 0].size)
            g_layer = new_img[:, :, 1].reshape(new_img[:, :, 1].size)
            b_layer = new_img[:, :, 2].reshape(new_img[:, :, 2].size)
            r_layer = r_layer[initialPoint_index:]
            g_layer = g_layer[initialPoint_index:]
            b_layer = b_layer[initialPoint_index:]
            endpoint = int(r_layer.size / step) * step
            r_layer = r_layer[:endpoint].reshape(int(r_layer.size / step), step)[:, 0]
            g_layer = g_layer[:endpoint].reshape(int(g_layer.size / step), step)[:, 0]
            b_layer = b_layer[:endpoint].reshape(int(b_layer.size / step), step)[:, 0]
        emb_to_r = np.bitwise_and(payload.content, 3)
        emb_to_g = np.right_shift(np.bitwise_and(payload.content, 12), 2)
        emb_to_b = np.right_shift(payload.content, 4)
        r_layer[:emb_to_r.size] = np.bitwise_or(np.bitwise_and(r_layer[:emb_to_r.size], 252), emb_to_r)
        g_layer[:emb_to_g.size] = np.bitwise_or(np.bitwise_and(g_layer[:emb_to_g.size], 252), emb_to_g)
        b_layer[:emb_to_b.size] = np.bitwise_or(np.bitwise_and(b_layer[:emb_to_b.size], 252), emb_to_b)
        return new_img

    def extractPayloadAdvanced(self):
        new_img = np.copy(self.img)
        r_layer, g_layer, b_layer = self.extract_rgb(new_img)
        ext_from_r = np.bitwise_and(r_layer, 3)
        ext_from_g = np.bitwise_and(g_layer, 3)
        ext_from_b = np.bitwise_and(b_layer, 3)
        ext_all = np.bitwise_or(np.bitwise_or(np.left_shift(ext_from_b, 4), np.left_shift(ext_from_g, 2)), ext_from_r)
        might_start = np.where(ext_all == 15)[0]
        find_flag = 1
        xml_start = np.array(
            [15, 3, 61, 56, 27, 22, 48, 32, 29, 38, 21, 50, 28, 54, 37, 47, 27, 35, 52, 34, 12, 18, 56, 48, 8, 34, 1,
             37, 27, 38, 13, 47, 25, 6, 37, 46, 25, 51, 52, 34, 21, 21, 17, 6, 11, 19, 32, 34, 15, 51])
        print(might_start)
        for i in might_start:
            step = 0
            while find_flag:
                step += 1
                if i + 50 * step > ext_all.size:
                    break
                for j in range(50):
                    if ext_all[i + j * step] != xml_start[j] :
                        break
                    if j == 49:
                        find_flag = 0
                        actual_start = i
                        actual_step = step
        if find_flag:
            print("cannot find the payload")
            return None
        else:
            ext_all = ext_all[actual_start:]
            endpoint = int(ext_all.size / actual_step) * actual_step
            ext_all = ext_all[:endpoint].reshape(int(ext_all.size / actual_step), actual_step)[:,0]
            return Payload(content=ext_all)


if __name__== "__main__":

    im = ndimage.imread("data/payload1.png")
    # im = ndimage.imread("small_img.jpeg")
    print(im.shape)

    payload = Payload(img=im,compressionLevel=6)
    im_content = payload.content

    # string_of_im_content = ",".join(im_content.astype('str'))

    # comp_data = np.array(list(map(int,string_of_im_content.split(","))),dtype=np.uint8)

    # comp_data1 = np.array(string_of_im_content.split(",")).astype(np.int)




    # payload1 = Payload(content=im_content)
    # im1 = payload1.img
    # print(np.array_equal(im,im1))

    # c_im = ndimage.imread("data/carrier1.png")
    # print(c_im.shape)
    # c = Carrier(c_im)
    # c1 = c.embedPayload(payload)
    # c2 = Carrier(c1)
    # c3 = c2.extractPayload()
    #print(c.clean())

    # cim = ndimage.imread("data/result1_9.png")
    # cim1 = Carrier(cim)
    # print(cim1.payloadExists())





    # r_layer = im[:,:,0]
    # print(r_layer.shape)
    # print(r_layer)

    # print(im[0][0][0])
    # print(im[1])
    # print(im[2])
    # payload = Payload(img=im2)

    # embedding
    # abc = np.arange(18).reshape(3, 6)
    # print(abc)
    # print(abc.reshape(int(abc.size/3),3))
    # r_l = abc.reshape(int(abc.size/3),3)[:,0]
    # print(r_l)
    # print(np.bitwise_and(abc, 3))
    # print(np.right_shift(np.bitwise_and(abc, 12), 2))
    # print(np.right_shift(np.bitwise_and(abc, 48), 4))
    # print(abc)

    #start_time = time.time()
    #print(time.time() - start_time)