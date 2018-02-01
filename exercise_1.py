import random
import sys

def exercise_1():
    try:
        while True:
            input_ip = input("\nEnter the IP address: ")
            octet_ip = input_ip.split(".")
            int_octet_ip = [int(i) for i in octet_ip]
            if (len(int_octet_ip) == 4) and \
                    (int_octet_ip[0] != 127) and \
                    (int_octet_ip[0] != 169) and  \
                    (0 <= int_octet_ip[1] <= 255) and \
                    (0 <= int_octet_ip[2] <=255) and \
                    (0 <= int_octet_ip[3] <= 255):
                break
            else:
                print ("Invalid IP, retry \n")
                continue
        masks = [0, 128, 192, 224, 240, 248, 252, 254, 255]
        while True:
            input_subnet = input("\nEnter the Subnet Mask: ")
            octet_subnet = [int(j) for j in input_subnet.split(".")]
            if (len(octet_subnet) == 4) and \
                    (octet_subnet[0] == 255) and \
                    (octet_subnet[1] in masks) and \
                    (octet_subnet[2] in masks) and \
                    (octet_subnet[3] in masks) and \
                    (octet_subnet[0] >= octet_subnet[1] >= octet_subnet[2] >= octet_subnet[3]):
                break
            else:
                print ("Invalid subnet mask, retry\n")
                continue
        ip_in_binary = []
        ip_in_bin_octets = [bin(i).split("b")[1] for i in int_octet_ip]

        for i in range(0,len(ip_in_bin_octets)):
            if len(ip_in_bin_octets[i]) < 8:
                padded_bin = ip_in_bin_octets[i].zfill(8)
                ip_in_binary.append(padded_bin)
            else:
                ip_in_binary.append(ip_in_bin_octets[i])

        ip_bin_mask = "".join(ip_in_binary)


        sub_in_bin = []
        sub_bin_octet = [bin(i).split("b")[1] for i in octet_subnet]
        for i in sub_bin_octet:
            if len(i) < 8:
                sub_padded = i.zfill(8)
                sub_in_bin.append(sub_padded)
            else:
                sub_in_bin.append(i)
        sub_bin_mask = "".join(sub_in_bin)
        #hosts
        no_zeros = sub_bin_mask.count("0")
        no_ones = 32 - no_zeros
        no_hosts = abs(2 ** no_zeros - 2)

        network_add_bin = ip_bin_mask[:no_ones] + "0" * no_zeros
        broadcast_add_bin = ip_bin_mask[:no_ones] + "1" * no_zeros

        network_add_bin_octet = []
        broadcast_binoct = []

        [network_add_bin_octet.append(i) for i in [network_add_bin[j:j+8]
        for j in range(0, len(network_add_bin), 8)]]
        [broadcast_binoct.append(i) for i in [broadcast_add_bin[j:j+8]
        for j in range(0,len(broadcast_add_bin),8)]]

        network_add_dec_final = ".".join([str(int(i,2)) for i in network_add_bin_octet])
        broadcast_add_dec_final = ".".join([str(int(i,2)) for i in broadcast_binoct])

        print ("\nThe entered ip address is: {0}".format(ip_in_bin_octets))
        print ("The Network address is: {0}/{1}".format(network_add_dec_final,no_ones))
        print ("The Broadcast address is: {0}/{1}".format(broadcast_add_dec_final, no_ones))
        list_ip = []
        print ("")
    except KeyboardInterrupt:
        print ("Interrupted by the User, exiting\n")
    except ValueError:
        print ("Seem to have entered an incorrect value, exiting\n")
if __name__ == '__main__':
    exercise_1()