class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = {}
        for i in range(0,len(strs)):
            clave = tuple(sorted(strs[i]))
            if clave in grupos:
                grupos[clave].append(strs[i])
            else:
                grupos[clave] = [strs[i]]
        return (list(grupos.values()))