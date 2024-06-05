import os
import src.gobuster
import src.metagoofil
import src.wget
import src.hydra
import src.whatweb
import src.herschel
import src.recon_ng
import src.dnsrecon
import src.websocket_client
import src.wfuzz
import src.curl 
import src.httprint  
import src.unicornscan  

def main():
    
    while True:
        print("Select an option:")
        print("1. Running metagoofil")
        print("2. wget")
        print("3. whatweb")
        print("4. Nmap")
        print("5. Nikto")
        print("6. SqlMap")
        print("7. dnsrecon")
        print("8. dnsenum")
        print("9. dirsearch")
        print("10. hydra")
        print("11. gobuster")
        print("12. recon_ng")
        print("13. websocket-client")
        print("14. wfuzz")
        print("15. Curl")
        # print("16. httprint")
        #print("17. Unicornscan")  
        print("16. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            src.metagoofil.main()
        elif choice == "2":
            src.wget.main()
        elif choice == "3":
            src.whatweb.main()
        elif choice == "4":
            src.herschel.run_nmap()
        elif choice == "5":
            src.herschel.run_nikto()
        elif choice == "6":
            src.herschel.run_sqlmap()
        elif choice == "7":
            src.dnsrecon.main()
        elif choice == "8":
            src.herschel.run_dnsenum()    
        elif choice == "9":
            src.herschel.run_dirsearch()
        elif choice == "10":
            src.hydra.main()
        elif choice == "11":
            src.gobuster.main()
        elif choice == "12":
            src.recon_ng.main()
        elif choice == "13":
            src.websocket_client.main()
        elif choice == "14":
            src.wfuzz.main()
        elif choice == "15":
            src.curl.curl_operations()  
        # elif choice == "16":
        #     for server in servers:
        #         src.httprint.main()
        # elif choice == "17":
        #     src.unicornscan.main()  
        elif choice == "16":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
