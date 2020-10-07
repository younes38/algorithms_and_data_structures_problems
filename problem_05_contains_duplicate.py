def containsDuplicate(self, arr):
        d = dict()
        
        for element in arr:
            if d.has_key(element):
                return True
            d[element] = True
            
        return False
