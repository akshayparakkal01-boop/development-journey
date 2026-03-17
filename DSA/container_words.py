source="traviduxtechnology"
target="vridautx"

class Containerword:
    def solution(self,source:str,target:str):
        present=True
        for ch in target:
            if ch not in source:
                present=False
                break
        return present
cw_instance=Containerword()
print(cw_instance.solution("traviduxtechnology","vridautx"))

