# Prosniff
This is a network traffic Sniffer to sniff out usernames and passwords or even sites visited by a person whether if you are performing a MITM attack or just want to sniff on your own network to see some stuff. Should be used for legal purposes only. This tool is for educational purposes and no Illegal activities should be done using this tool.


The usage is simple. 
It will ask you the interface to sniff on. just enter it and the sniffer will start. If that interface is not there or wrong the sniffer will not work.

**If you encounter an error like this**

Exception ignored in: <bound method SuperSocket.__del__ of <scapy.arch.linux.L2ListenSocket object at 0x7f7ca13086a0>>
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/scapy/supersocket.py", line 134, in __del__
    self.close()
  File "/usr/local/lib/python3.6/dist-packages/scapy/arch/linux.py", line 514, in close
    set_promisc(self.ins, self.iface, 0)
  File "/usr/local/lib/python3.6/dist-packages/scapy/arch/linux.py", line 165, in set_promisc
    mreq = struct.pack("IHH8s", get_if_index(iff), PACKET_MR_PROMISC, 0, b"")
  File "/usr/local/lib/python3.6/dist-packages/scapy/arch/linux.py", line 380, in get_if_index
    return int(struct.unpack("I", get_if(iff, SIOCGIFINDEX)[16:20])[0])
  File "/usr/local/lib/python3.6/dist-packages/scapy/arch/common.py", line 59, in get_if
    ifreq = ioctl(sck, cmd, struct.pack("16s16x", iff.encode("utf8")))
OSError: [Errno 19] No such device

This is a scapy module issue 
kindly make the following changes in 
/usr/lib/python-3/dist-packages/scapy/arch/linux.py
on line 497 or 515 
change  except AttributeError: to except (AttributeError, OSError):


For more info on the error kindly visit 
for the issue: 
  https://github.com/secdev/scapy/issues/2470
and for the solution for the issue: 
  https://github.com/secdev/scapy/pull/2471/commits/55f2e735e8b7e41152b95051f4c16dc3eadcb6d6
  
  
  This is how the tool looks 
  ![Screenshot](https://github.com/Sarthak044/Prosniff/blob/main/img/prosniff.jpg)
