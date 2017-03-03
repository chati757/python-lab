# My keyboard is set to the English - United States keyboard
import ctypes
# For debugging Windows error codes in the current thread
user32 = ctypes.WinDLL('user32', use_last_error=True)
curr_window = user32.GetForegroundWindow()
thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
# Made up of 0xAAABBBB, AAA = HKL (handle object) & BBBB = language ID
klid = user32.GetKeyboardLayout(thread_id)
#67699721
# Language ID -> low 10 bits, Sub-language ID -> high 6 bits
# Extract language ID from KLID
lid = klid & (2**16 - 1)
# Convert language ID from decimal to hexadecimal
lid_hex = hex(lid)
#'0x409'
print(lid_hex)
'''
# I switched my keyboard to the Russian keyboard
curr_window = user32.GetForegroundWindow()
thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
klid = user32.GetKeyboardLayout(thread_id)
68748313
# Extract language ID from KLID
lid = klid & (2**16 - 1)
# Convert language ID from decimal to hexadecimal
lid_hex = hex(lid)
#'0x419'
'''