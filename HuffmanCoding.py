from typing import Any
import heapq

class HuffmanCoding:
    '''
    def frequency(text):
        # Take a text string and determine the frequencies of the characters
        frequency = {}
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        lst = [(v, k) for k, v in frequency.items()]
        # Build and sort a list of tuples from lowest to highest frequencies
        lst.sort(reverse=True)
        return lst
    '''

    def build(self, text: str) -> Any:
        freq = {}
        for i in range(len(text)):
            freq[text[i]] = 0

        for t in text:
            freq[t] += 1

        # print(freq)

        heap = [[value, [key, ""]] for key, value in freq.items()]
        heapq.heapify(heap)

        # Huffman Encoding Algorithm
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            for k in left[1:]:
                k[1] = '0' + k[1]
            for k in right[1:]:
                k[1] = '1' + k[1]
            heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

        dict_sorted = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

        for i in range(len(dict_sorted)):
            freq[dict_sorted[i][0]] = dict_sorted[i][1]

        freq = dict(sorted(freq.items(), key=lambda item: item[1]))
        encoded = self.encode(freq, text)
        decoded = self.decode(freq, encoded)
        return freq

    ''' 
    def extractMin(self, queue):
        p = [v for k, v in queue]
        return queue.pop(p.index(min(p)))
    '''

    def encode(self, Dic: Any, text: str) -> str:
       # Return string for encoding
        encoded = ""
        for i in text:
            encoded = encoded + Dic[i]
        return encoded


    @staticmethod
    def decode(Dic: Any, text: str) -> str:
        new = dict([(value, key) for key, value in Dic.items()])
        decoded = ""
        tmp_decode = ""

        encoded_chars = []

        for key, value in new.items():
            encoded_chars.append(key)

        for i in text:
            tmp_decode += i
            if tmp_decode in encoded_chars:
                decoded += new[tmp_decode]
                tmp_decode = ""
            else:
                continue
        return decoded
