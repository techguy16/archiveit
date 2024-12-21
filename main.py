import handlers.youtube,handlers.data
from colorama import Fore, Style

print(f"{Style.BRIGHT}{Fore.GREEN}ArchiveIt {Style.RESET_ALL}{Fore.BLUE}v{handlers.data.VERSION}\n")
print(f"{Fore.MAGENTA}What would you like to do?{Style.RESET_ALL}")
print(f"   {Style.BRIGHT}1.{Style.RESET_ALL} Recover YouTube Video\n")
option = input(f"{Style.BRIGHT}{Fore.RED}Choose option (1) > {Style.RESET_ALL}")

if option == "1":
    available = handlers.youtube.request_availability(input(f"\n{Style.BRIGHT}{Fore.MAGENTA}Paste in video URL or ID > {Style.RESET_ALL}"))
    if not available == False:
        saveas = input(f"{Fore.RED}{Style.BRIGHT}Video has been archived! {Style.RESET_ALL}{Fore.GREEN}Please provide a file name to save to > {Style.RESET_ALL}")
        print(f"{Style.BRIGHT}{Fore.MAGENTA}Downloading...", end='\r')
        handlers.youtube.download_video(available,saveas)
        print(f"{Style.BRIGHT}{Fore.MAGENTA}Downloading... Done!")
        