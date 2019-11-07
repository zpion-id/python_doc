## File

```py
import os
import time

print(os.path.getsize("format.py")) # 1634 (satuan byte)

print(os.stat("format.py"))
# os.stat_result(st_mode=33279, st_ino=95832, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000, st_size=1634, st_atime=1573136676, st_mtime=1573136676, st_ctime=1573136676)

st_size = os.stat("format.py").st_size
st_mode = os.stat("format.py").st_mode
st_atime = os.stat("format.py").st_atime
st_mtime = os.stat("format.py").st_mtime
st_mtime_ns = os.stat("format.py").st_mtime_ns
st_ctime = os.stat("format.py").st_ctime

print(st_size) # 1634 (satuan byte)
print(st_mode) # 33279
print(st_atime) # 1573136676.9137497
print(st_mtime) # 1573136676.6588533
print(st_mtime_ns) # 1573136676658853300
print(st_ctime) # 1573136676.6588533

print(time.localtime(st_atime))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=7, tm_hour=21, tm_min=39, tm_sec=56, tm_wday=3, tm_yday=311, tm_isdst=0)
print(time.localtime(st_atime).tm_year) # 2019

print(time.localtime(st_mtime))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=7, tm_hour=21, tm_min=39, tm_sec=55, tm_wday=3, tm_yday=311, tm_isdst=0)

#print(time.localtime(st_mtime_ns)) # OSError: [Errno 75] Value too large for defined data type

print(time.localtime(st_ctime))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=7, tm_hour=21, tm_min=39, tm_sec=55, tm_wday=3, tm_yday=311, tm_isdst=0)
```
