import numpy as np
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

print(np.mean(english_score),np.max(english_score),np.min(english_score),np.std(english_score))
print(np.mean(math_score),np.max(math_score),np.min(math_score),np.std(math_score))
print(np.mean(chinese_score),np.max(chinese_score),np.min(chinese_score),np.std(chinese_score))
math_score[4]=55
print(np.mean(math_score),np.max(math_score),np.min(math_score),np.std(math_score))

print(np.corrcoef(english_score,chinese_score))
print(np.corrcoef(math_score,chinese_score))