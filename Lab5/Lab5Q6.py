import math
def number_tdma_users (s_s, g_s, u_s):
    result = math.floor(s_s / (g_s + u_s))
    return result
    

print (number_tdma_users(0.1, 0.001, 0.001))
	