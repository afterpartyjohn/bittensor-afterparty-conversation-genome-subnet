
class Utils:
    @staticmethod
    def get(inDict, path, default=None, dataType=None):
        if not inDict:
            return default
        out = default
        parts = path.split(".")
        cur = inDict
        success = True
        for part in parts:
            #print(part, cur, part in cur, type(cur)==dict)
            if cur and type(cur)==list:
                index = 0
                try:
                    part = int(part)
                except:
                    pass
            if cur and ( (type(cur)==dict and part in cur) or (type(cur)==list and  0 <= part < len(cur)) ):
                cur = cur[part]
            else:
                success = False
                break
        if success:
            out = cur
        if dataType:
            if dataType == 'int':
                out2 = default
                try:
                    out2 = int(out)
                except:
                    pass
                out = out2
        return out

    @staticmethod
    def compare_arrays(arr1, arr2):
        result_dict = {}

        set1 = set(arr1)
        set2 = set(arr2)

        result_dict["both"] = list(set1.intersection(set2))
        result_dict["unique_1"] = list(set1.difference(set2))
        result_dict["unique_2"] = list(set2.difference(set1))

        return result_dict

    @staticmethod
    def pluck(dicts, key):
        values = []
        for dictionary in dicts:
            if key in dictionary:
                values.append(dictionary[key])
        return values

    @staticmethod
    def guid():
        current_time = int(round(time.time() * 1000))
        guid = uuid.uuid1(node=current_time)
        guid_int = int(guid.int)
        return guid_int

    @staticmethod
    def split_overlap_array(array, size=10, overlap=2):
        result = []
        lenArray = len(array)
        num_splits = lenArray//(size-overlap) + 1

        for i in range(num_splits):
            start = i*(size-overlap)
            end = start + size
            window = array[start:end]
            #print("Start/end/elements", start, end, window)
            result.append(array[start:end])
            if end >= lenArray:
                break
        return result

    @staticmethod
    def is_empty_vector(vector):
        return all(v == 0.0 for v in vector)

