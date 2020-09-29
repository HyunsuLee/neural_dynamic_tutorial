import numpy as np
import matplotlib.pyplot as plt

U_REST = -65 # mV
THRESHOLD = -40 #mV
DT = 1 # ms
T_START = 0 # ms
T_END = 6000 # ms
TAU = 20 # ms, membrane time constant
R_M = 100 # MOhm
I_SQUARE_PEAK = 0.5 # nA
u = -65 # mV, starting potential
t = 0
TIME_X = np.arange(T_START, T_END, DT) 

i_input = np.zeros((6000))
i_input[100:200] = I_SQUARE_PEAK

# LIF equation
def du_dt(U_REST, u, R_M, i_input, TAU):
    return (-(u - U_REST) + (R_M * i_input))/TAU


# Euler method
def euler(u, du_dt, DT):
    return u + du_dt*DT


u_trace = np.zeros((6000))
next_u = u
peak_time = []

for t in range(T_END):
    u_trace[t] = next_u
    temp_du_dt = du_dt(U_REST, next_u, R_M, i_input[t], TAU)
    next_u = euler(next_u, temp_du_dt, DT)
    if next_u > THRESHOLD:
        next_u = U_REST
        peak_time.append(t)
    else:
        pass

plt.plot(TIME_X, u_trace,'b-')
plt.xlim(80, 250)
plt.savefig('./test.png')

delta_t_peak = peak_time[1] - peak_time[0]
print(delta_t_peak)
