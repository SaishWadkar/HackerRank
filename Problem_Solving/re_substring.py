import re

s='acskesrsrsdank'

pattern =r'.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*'

output = re.search(pattern,s)
if output:
    print("YES")