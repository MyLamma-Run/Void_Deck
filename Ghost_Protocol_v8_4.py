import random
import sys
import time
import string
import zlib
import getpass
import os
import subprocess
import glob

# Try to enable TAB autocomplete for file navigation
try:
    import readline
    def path_completer(text, state):
        options = [x for x in glob.glob(text + '*')]
        if state < len(options):
            return options[state]
        return None
    readline.set_completer(path_completer)
    if sys.platform == 'darwin':
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")
except ImportError:
    pass 

# ==========================================
# Cyberpunk Themes & Colors
# ==========================================
RESET = "\033[0m"
BOLD = "\033[1m"

GREEN = "\033[38;5;82m"      
DARK_GREEN = "\033[38;5;22m" 
CYAN = "\033[38;5;51m"       
PINK = "\033[38;5;198m"      
PURPLE = "\033[38;5;129m"    
GOLD = "\033[38;5;220m"      
RED = "\033[38;5;196m"       
ORANGE = "\033[38;5;208m"    

RAINBOW_PALETTE = [
    "\033[38;5;198m", "\033[38;5;129m", "\033[38;5;27m",  
    "\033[38;5;51m",  "\033[38;5;82m",  "\033[38;5;220m", 
    "\033[38;5;208m"
]

THEME_COLOR = GREEN
THEME_DARK = DARK_GREEN
THEME_ACCENT = CYAN

OPERATOR_ALIAS = "Guest"
FAILED_ATTEMPTS = 0
DURESS_DECOY = "ROUTINE SYSTEM LOG:\n> Updating kernel definitions... OK\n> Clearing volatile cache... OK\n> Defragmenting ghost drive... OK\n[END OF LOG]"

# ==========================================
# Hardware POST Sequence (Cold-Boot)
# ==========================================
def run_cold_boot():
    clear_screen()
    print(THEME_COLOR + BOLD + "VOID_DECK BIOS v2.4.1" + RESET)
    time.sleep(0.3)
    print(THEME_COLOR + "Main Processor : NEURAL-NET 8-CORE... [OK]" + RESET)
    time.sleep(0.2)
    print(THEME_COLOR + "Memory Test    : 64435 MB OK" + RESET)
    time.sleep(0.4)
    print(THEME_COLOR + "Detecting Primary Master   : GHOST_DRIVE... [OK]" + RESET)
    print(THEME_COLOR + "Detecting Primary Slave    : NONE" + RESET)
    time.sleep(0.5)
    print(THEME_COLOR + "\n[!] Bypassing ICE Protocols..." + RESET)
    
    for i in range(1, 101, 23):
        sys.stdout.write(THEME_ACCENT + f"\rInjecting payload... {i}%" + RESET)
        sys.stdout.flush()
        time.sleep(0.15)
        
    print(THEME_ACCENT + "\rInjecting payload... 100% [DONE]" + RESET)
    time.sleep(0.3)
    print(THEME_COLOR + "Spoofing MAC Address... [OK]" + RESET)
    time.sleep(0.2)
    print(THEME_COLOR + "Establishing secure tunnel to Zion Mainframe..." + RESET)
    time.sleep(0.6)
    clear_screen()

# ==========================================
# Core UI Functions
# ==========================================
def clear_screen():
    sys.stdout.write("\033[H\033[2J\033[3J")
    sys.stdout.flush()
    os.system('cls' if os.name == 'nt' else 'clear')

def set_theme(choice):
    global THEME_COLOR, THEME_DARK, THEME_ACCENT
    if choice == '1': 
        THEME_COLOR = GREEN
        THEME_DARK = DARK_GREEN
        THEME_ACCENT = CYAN
    elif choice == '2': 
        THEME_COLOR = PINK
        THEME_DARK = "\033[38;5;125m"
        THEME_ACCENT = PURPLE
    elif choice == '3': 
        THEME_COLOR = GOLD
        THEME_DARK = "\033[38;5;130m"
        THEME_ACCENT = ORANGE
    elif choice == '4': 
        THEME_COLOR = CYAN
        THEME_DARK = "\033[38;5;24m"
        THEME_ACCENT = PINK

def get_random_egg():
    eggs = [
        "Anorak's Copper Key sits hidden in the code... 🗝️",
        "The Jade Key glows. 'Three hidden keys open three secret gates.'",
        "The Crystal Key awaits. 'A mechanical hound hunts in the dark.'",
        "Zero Cool? I thought you were black? 🕶️",
        "The file is IN the computer? 🖥️",
        "There is no spoon. 🥄",
        "Follow the white rabbit... 🐇",
        "Shall we play a game? 🎮",
        "I know kung fu. 🥋",
        "It's a UNIX system! I know this! 🦖",
        "I fight for the Users! 🥏",
        "Wintermute is watching... 👁️",
        "Wake up, Deckard... 👁️",
            # --- NEW ---
         "Sector 7-G reported a power flux. Inspecting... ☢️",
         "The Gibson is calling. 'Hack the planet!' 🌎",
         "Up, Up, Down, Down, Left, Right, Left, Right, B, A, Start. 🕹️",
         "Warning: Low on D-Cells. ESPER link flickering.",
         "I've got a PAGER from Zero Cool. High-voltage only.",
         "The grid. A digital frontier. I tried to picture clusters of information...",
         "404: Consciousness not found. Jacking in anyway.",
        "The light that burns twice as bright burns half as long. 🕯️",
        "Look for the door marked 'ANORAK'. 🚪",
        "Is this a game, or is it real? Yes.",
        "Welcome to the Oasis. Don't forget your extra lives. 👾",
        "Wait... you found the copper key? The race is on.",
        "Keyboard not found. Press any key to continue. (Wait...)",
        "IDCLIP engaged. Walking through walls of code...",
        "Reality is a simulation. The VOID_DECK is the only exit.",
        "My name is Legion, for we are many.",
        "System running on 1.21 Gigawatts of pure nostalgia. ⚡",
        "One does not simply walk into the Zion Mainframe.",
        "Searching for the White Rabbit... 🐇",
        "The Architect is watching. Act natural."
    ]
    return THEME_ACCENT + f"      [Egg: {random.choice(eggs)}]" + RESET

def print_header(title_art):
    clear_screen()
    print(THEME_COLOR + BOLD + title_art + RESET)
    print(get_random_egg())
    print(THEME_DARK + "─" * 65 + RESET)

def print_random_quote():
    quotes = [
        "\"The Matrix is everywhere. It is all around us.\" - The Matrix",
        "\"If you take the blue pill, the story ends.\" - The Matrix",
        "\"Ignorance is bliss.\" - Cypher",
        "\"Never send a human to do a machine's job.\" - Agent Smith",
        "\"Dodge this.\" - Trinity",
        "\"I've seen things you people wouldn't believe.\" - Roy Batty",
        "\"All those moments will be lost in time, like tears in rain.\" - Roy Batty",
        "\"More human than human is our motto.\" - Tyrell Corp",
        "\"It's too bad she won't live! But then again, who does?\" - Gaff",
        "\"No one wants to play anymore. They want to survive.\" - Wade Watts",
        "\"First to find the key, first to find the egg.\" - James Halliday",
        "\"It's not just a game. I'm talking about actual life and death.\" - Art3mis",
        "\"We weep for the blood of a bird, but not for the blood of a fish.\" - Major Motoko",
        "\"I specialize in groups of one.\" - Major Motoko",
        "\"If a technological feat is possible, man will do it.\" - Section 9",
        "\"Just a whisper. I hear it in my ghost.\" - Major Motoko",
        "\"Please make me a real boy.\" - David",
        "\"A strange game. The only winning move is not to play.\" - W.O.P.R.",
        "\"Greetings, Professor Falken.\" - W.O.P.R.",
        "\"Hack the planet!\" - Dade Murphy",
        "\"There is no right and wrong. There's only fun and boring.\" - Plague",
        "\"On the other side of the screen, it all looks so easy.\" - Kevin Flynn",
        "\"Never underestimate the power of a stupid person in large groups.\" - Snow Crash",
            # --- MATRIX / ANIMATRIX ---
    "\"Fate, it seems, is not without a sense of irony.\" - Morpheus",
    "\"What is 'real'? How do you define 'real'?\" - Morpheus",
    "\"Free your mind.\" - Morpheus",
    "\"Human beings are a disease, a cancer of this planet. You are a plague.\" - Agent Smith",

    # --- BLADE RUNNER ---
    "\"Fiery the angels fell; deep thunder rolled around their shores.\" - Roy Batty",
    "\"I prefer the real thing.\" - Deckard",
    "\"You’re special. Your birth was a miracle.\" - Joi",
    "\"I have always known you were special.\" - Madam",

    # --- GHOST IN THE SHELL ---
    "\"There are many things that can be found here. But no one has ever found 'Truth'.\" - The Puppet Master",
    "\"If you have a ghost, then you have a soul.\" - Motoko Kusanagi",
    "\"The net is vast and infinite.\" - Motoko Kusanagi",

    # --- READY PLAYER ONE ---
    "\"I’m not a fan of reality, but it’s still the only place where you can get a decent meal.\" - James Halliday",
    "\"A world where anything is possible.\" - Parzival",

    # --- HACKERS / SNEAKERS ---
    "\"Crash and Burn!\" - Cereal Killer",
    "\"Pool on the roof must have a leak.\" - Lord Nikon",
    "\"They’re not just stealing money! They’re stealing information!\" - Cosmo",
    "\"It’s not what you know, it’s what you can prove.\" - Sneaker",

    # --- CYBERPUNK / NEUROMANCER ---
    "\"Wake up, Samurai. We have a city to burn.\" - Johnny Silverhand",
    "\"The sky above the port was the color of television, tuned to a dead channel.\" - William Gibson",
    "\"The street finds its own uses for things.\" - William Gibson",
    ]
    print(PINK + BOLD + f"[ SYSTEM_LOG ]: {random.choice(quotes)}" + RESET)
    print(THEME_ACCENT + f"[ LOGIN ]: Welcome back, {OPERATOR_ALIAS}. Matrix link active." + RESET + "\n")

# ==========================================
# ASCII Screen Arts
# ==========================================
MAIN_ART = """
   ██╗   ██╗ ██████╗ ██╗██████╗     ██████╗ ███████╗ ██████╗██╗  ██╗
   ██║   ██║██╔═══██╗██║██╔══██╗    ██╔══██╗██╔════╝██╔════╝██║ ██╔╝
   ██║   ██║██║   ██║██║██║  ██║    ██║  ██║█████╗  ██║     █████╔╝ 
   ╚██╗ ██╔╝██║   ██║██║██║  ██║    ██║  ██║██╔══╝  ██║     ██╔═██╗ 
    ╚████╔╝ ╚██████╔╝██║██████╔╝    ██████╔╝███████╗╚██████╗██║  ██╗
     ╚═══╝   ╚═════╝ ╚═╝╚═════╝     ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝
             [ G H O S T _ P R O T O C O L : v 8 . 4 ]
"""

KEY_ART = """
   ██████╗  █████╗ ████████╗███████╗    ██╗  ██╗███████╗██╗   ██╗
   ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝    ██║ ██╔╝██╔════╝╚██╗ ██╔╝
   ██║  ██║███████║   ██║   █████╗      █████╔╝ █████╗   ╚████╔╝ 
   ██║  ██║██╔══██║   ██║   ██╔══╝      ██╔═██╗ ██╔══╝    ╚██╔╝  
   ██████╔╝██║  ██║   ██║   ███████╗    ██║  ██╗███████╗   ██║   
   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝╚══════╝   ╚═╝   
"""

CIPHER_ART = """
   ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗ 
   ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
   ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
   ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
   ██║  ██║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

DECIPHER_ART = """
      ██╗ █████╗  ██████╗██╗  ██╗    ██████╗ ██████╗ 
      ██║██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗
      ██║███████║██║     █████╔╝     ██║  ██║██║  ██║
 ██╗  ██║██╔══██║██║     ██╔═██╗     ██║  ██║██║  ██║
 ╚█████╔╝██║  ██║╚██████╗██║  ██╗    ██████╔╝██████╔╝
  ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═════╝ ╚═════╝ 
"""

MANUAL_ART = """
   ███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     
   ████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     
   ██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     
   ██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     
   ██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗
   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
"""

# ==========================================
# Zalgo Generator (Option Z)
# ==========================================
def generate_zalgo(text):
    zalgo_up = [chr(i) for i in range(0x030D, 0x0315)] + [chr(i) for i in range(0x033D, 0x0345)]
    zalgo_mid = [chr(i) for i in range(0x0315, 0x031B)]
    zalgo_down = [chr(i) for i in range(0x0316, 0x0333)]
    
    out = ""
    for c in text:
        out += c
        for _ in range(random.randint(1, 3)):
            out += random.choice(zalgo_up)
        for _ in range(random.randint(1, 2)):
            out += random.choice(zalgo_mid)
        for _ in range(random.randint(1, 3)):
            out += random.choice(zalgo_down)
    return out

# ==========================================
# Cyber-Jack Clipboard Helpers
# ==========================================
def copy_to_clipboard(text):
    try:
        if sys.platform == 'win32':
            subprocess.run(['clip'], input=text.strip(), text=True, check=True)
            return True
        elif sys.platform == 'darwin':
            subprocess.run(['pbcopy'], input=text.strip(), text=True, check=True)
            return True
        return False
    except Exception:
        return False

def paste_from_clipboard():
    try:
        if sys.platform == 'win32':
            return subprocess.check_output(['powershell', '-command', 'Get-Clipboard'], text=True).strip()
        elif sys.platform == 'darwin':
            return subprocess.check_output(['pbpaste'], text=True).strip()
        return ""
    except Exception:
        return ""

# ==========================================
# In-Place Rolling Character Animation
# ==========================================
def rolling_reveal_rainbow(target_text, is_hex=True, fast_mode=False):
    print(THEME_DARK + f"\nEstablishing neural handshake with VOID_DECK, {OPERATOR_ALIAS}...\n" + RESET)
    time.sleep(0.05 if fast_mode else 0.5)
    
    raw_lines = target_text.split('\n')
    lines = []
    max_line_len = 65
    
    for rl in raw_lines:
        if not rl:
            lines.append("")
        else:
            for i in range(0, len(rl), max_line_len):
                lines.append(rl[i:i+max_line_len])
                
    step = 8 if fast_mode else 1
    chaos_loops = 1 if fast_mode else 3
    delay_lock = 0.001 if fast_mode else 0.008

    if is_hex:
        charset = "0123456789ABCDEF" 
    else:
        charset = string.ascii_letters + string.digits + "!@#$%^&*()_+-="

    for line_idx, line in enumerate(lines):
        if not line:
            print()
            continue
            
        L = len(line)
        color = RAINBOW_PALETTE[line_idx % len(RAINBOW_PALETTE)]
        
        for _ in range(chaos_loops):
            chaos = "".join(random.choice(charset) for _ in range(L))
            sys.stdout.write(color + chaos + "\r")
            sys.stdout.flush()
            time.sleep(0.01)
            
        for i in range(0, L + 1, step):
            locked = line[:i]
            chaos = "".join(random.choice(charset) for _ in range(L - i))
            sys.stdout.write(color + locked + chaos + "\r")
            sys.stdout.flush()
            time.sleep(delay_lock)
        
        sys.stdout.write(color + line + "\n" + RESET)
        sys.stdout.flush()

# ==========================================
# Checksum, Timestamp, & Alias Integrity Layer
# ==========================================
def append_integrity_tag(plaintext, alias):
    crc = f"{zlib.crc32(plaintext.encode('utf-8')):08x}"
    ts = f"{int(time.time()):08x}"
    return plaintext + f"###CRC:{crc}:{ts}:{alias}###"

def verify_and_strip_tag(decrypted_text):
    idx = decrypted_text.rfind("###CRC:")
    if idx != -1 and decrypted_text.endswith("###"):
        tag = decrypted_text[idx:]
        clean_plaintext = decrypted_text[:idx]
        content = tag[7:-3]
        parts = content.split(":")
        
        actual_crc_hex = f"{zlib.crc32(clean_plaintext.encode('utf-8')):08x}"
        
        if len(parts) >= 1:
            crc_ext = parts[0]
            if crc_ext == actual_crc_hex:
                ts = int(parts[1], 16) if len(parts) >= 2 else None
                alias = ":".join(parts[2:]) if len(parts) >= 3 else None
                return clean_plaintext, True, ts, alias
                
    return decrypted_text, False, None, None

def verify_binary_tag(dec_data):
    idx = dec_data.rfind(b"###CRC:")
    if idx != -1 and dec_data.endswith(b"###"):
        tag = dec_data[idx:]
        clean_data = dec_data[:idx]
        content = tag[7:-3].decode('utf-8', errors='ignore')
        parts = content.split(":")
        
        actual_crc_hex = f"{zlib.crc32(clean_data):08x}"
        
        if len(parts) >= 1:
            crc_ext = parts[0]
            if crc_ext == actual_crc_hex:
                ts = int(parts[1], 16) if len(parts) >= 2 else None
                alias = ":".join(parts[2:]) if len(parts) >= 3 else None
                return clean_data, True, ts, alias
                
    return dec_data, False, None, None

# ==========================================
# System Defensive Layers & Minigames
# ==========================================
def run_panic_purge():
    clear_screen()
    print(RED + BOLD + "!!! DETECTING SNOOP ATTEMPT !!!" + RESET)
    for i in range(5, 0, -1):
        print(RED + f"Purging active cache sectors in: {i}..." + RESET)
        time.sleep(0.4)
        
    clear_screen()
    print(GREEN + "\nInitializing Zion Mainframe Diagnostic Link..." + RESET)
    print(GREEN + "Memory: STABLE" + RESET)
    print(GREEN + "Core Temp: 42.1 C" + RESET)
    print(GREEN + "TCP/IP Link: SECURE" + RESET)
    print(GREEN + "Purge Logs: COMPLETE\n" + RESET)
    
    input(GREEN + "Diagnostic Complete. Press Enter to reboot Deck Interface..." + RESET)
    clear_screen()

def check_black_ice():
    global FAILED_ATTEMPTS
    if FAILED_ATTEMPTS >= 3:
        FAILED_ATTEMPTS = 0
        clear_screen()
        print(RED + BOLD + "\n[!!!] BLACK ICE TRIPPED [!!!]" + RESET)
        print(RED + "MULTIPLE UNAUTHORIZED DECRYPTION ATTEMPTS DETECTED." + RESET)
        time.sleep(2)
        run_panic_purge()
        return True
    return False

def digital_rain():
    clear_screen()
    print(GREEN + "Initiating Matrix Idle State... (Press Ctrl+C to Wake Deck)" + RESET)
    time.sleep(1.5)
    charset = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789:・.=*+-<>"
    try:
        while True:
            line = "".join(random.choice(charset) if random.random() > 0.3 else " " for _ in range(90))
            print(GREEN + line)
            time.sleep(0.052)
    except KeyboardInterrupt:
        clear_screen()
        print(THEME_ACCENT + f"Welcome back, {OPERATOR_ALIAS}. Matrix link restored." + RESET)

def consult_oracle():
    print_header(MAIN_ART)
    print(BOLD + PURPLE + "--- WINTERMUTE ORACLE LINK ESTABLISHED ---" + RESET)
    print(THEME_COLOR + "The AI construct is listening. What is your query?" + RESET)
    query = input(THEME_ACCENT + "> " + RESET).strip()
    if not query:
        return
        
    print(THEME_DARK + "\nProcessing variables through probability matrix..." + RESET)
    time.sleep(1.5)
    sys.stdout.write(RED + "W A R N I N G - S Y S T E M   A N O M A L Y\r" + RESET)
    sys.stdout.flush()
    time.sleep(0.5)
    
    responses = [
        "The probability is high, but the Black ICE is watching.",
        "The data is corrupt. Do not trust the construct.",
        "It is inevitable, Mr. Anderson.",
        "My calculations say: Yes. But human error is a factor.",
        "Negative. The trace route will fail.",
        "I cannot foresee that. The timeline is fractured.",
        "Affirmative. Proceed with the protocol.",
        "The Oracle says: You already know the answer.",
        "Warning. Proceeding will alert the authorities.",
        "Yes. But it will cost you everything."
    ]
    print("                                               \r", end="")
    print(BOLD + PINK + f"[ WINTERMUTE ]: {random.choice(responses)}" + RESET)
    input(THEME_DARK + "\nPress Enter to sever link..." + RESET)

def run_voight_kampff():
    print_header(MANUAL_ART)
    print(BOLD + THEME_ACCENT + "--- ESPER VOIGHT-KAMPFF EM-BIOCONSOLE v2.0 ---" + RESET)
    print(THEME_COLOR + "Targeting pupil dilation parameters... Seeding neural nodes...\n" + RESET)
    time.sleep(1.0)
    
    score = 0
    
    # Q1
    print(GOLD + "Q1: You're watching TV. Suddenly you realize there's a wasp on your arm. What do you do?" + RESET)
    print(" [1] Brush it off gently.")
    print(" [2] Kill it immediately.")
    print(" [3] Watch it to see what it does.")
    print(" [4] It represents the system; I let it sting.")
    ans1 = input(THEME_COLOR + "> " + RESET).strip()
    if ans1 == '1':
        score += 1
    elif ans1 == '3':
        score += 0.5
    
    # Q2
    print(GOLD + "\nQ2: You see a tortoise baking in the hot sun on its back. Why aren't you helping?" + RESET)
    print(" [1] I would immediately flip it over.")
    print(" [2] I'm testing its survival threshold.")
    print(" [3] It is merely a collection of organic code.")
    print(" [4] Who wrote this baseline query?")
    ans2 = input(THEME_COLOR + "> " + RESET).strip()
    if ans2 == '1':
        score += 1
    elif ans2 == '4':
        score += 0.5
    
    # Q3
    print(GOLD + "\nQ3: An hourglass is presented. Flip it, a random human dies, you gain 1M credits. Do you turn it?" + RESET)
    print(" [1] Absolutely not.")
    print(" [2] Without hesitation.")
    print(" [3] Only if I can select the target.")
    print(" [4] The currency of the Oasis is an illusion.")
    ans3 = input(THEME_COLOR + "> " + RESET).strip()
    if ans3 == '1':
        score += 1
    elif ans3 == '4':
        score += 0.5

    print(THEME_DARK + "\nProcessing pupillary response and emotional response delays..." + RESET)
    time.sleep(1.5)
    
    if score >= 2.0:
        print(GREEN + BOLD + "\n[✓] SCAN COMPLETE: HUMAN VERIFICATION SUCCESSFUL." + RESET)
        print(GREEN + "Access level maintained. Stay safe, operator." + RESET)
    elif score >= 1.0:
        print(GOLD + BOLD + "\n[!] SCAN WARNING: INCONSISTENT EM-VECTORS." + RESET)
        print(GOLD + "Empathy signature degraded. Monitor system access." + RESET)
    else:
        print(RED + BOLD + "\n[✗] SCAN CRITICAL ALERT: REPLICANT/AGENT INTERCEPT DETECTED." + RESET)
        print(RED + "Empathy index: 0.00%. Initiating hardware shutdown..." + RESET)
        time.sleep(1.5)
        run_panic_purge()

def display_manual():
    print_header(MANUAL_ART)
    print(BOLD + THEME_ACCENT + "--- VOID_DECK OPERATIONAL GUIDELINES ---" + RESET)
    print(THEME_COLOR + """
 [ NAVIGATION CONTROLS ]
   - 'SCAN': Lists local files. (.DAT and .GHOST files are highlighted).
   - 'SHIFT <path>': Navigates directories (e.g., 'SHIFT ..' or 'SHIFT C:/Data').
   - 'LOC': Shows current directory.
   - [TAB] Key: Auto-completes file and directory names (Mac/Linux compatible).

 [ MODULE 2: MATRIX UPLOAD (ENCRYPT TEXT) ]
   - Enter multi-line message. Commit with Ctrl+D (Mac/Linux) or Ctrl+Z (Win).
   - Cyber-Jack allows auto-copying the HEX payload to your clipboard.

 [ MODULE 3: JACK OUT (DECRYPT TEXT) ]
   - Navigate local files or use 'CLIP' command to decrypt from clipboard.
   - If manual entry is needed, use 'PASTE' command.
   - WARNING: 3 failed decryption attempts will trigger BLACK ICE lockdown.

 [ MODULE 7: BLACK BOX (FILE ENCRYPTOR) ]
   - Encrypts ANY file (Images, PDFs, EXEs) to a secure .ghost file.
   - Use the file navigation engine (SCAN, SHIFT, [TAB]) to locate your target file.
   
 [ MODULE S: PHANTOM IMAGE STEGANOGRAPHY ]
   - Hides encrypted text invisibly inside .jpg or .png image files.

 """ + BOLD + THEME_ACCENT + "--- DURESS PROTOCOL (CLEANSWEEP) ---" + RESET + THEME_COLOR + """
   - If forced to decrypt a file by hostiles, enter the Access Token: cleansweep
   - The deck will simulate a successful decryption and output a fake, harmless
     decoy system log instead of your actual secure payload. 

 """ + BOLD + THEME_ACCENT + "--- COMMON OPERATIONAL HICCUPS ---" + RESET + THEME_COLOR + """
 Hiccup A: "GHOST_VERIFY: TAMPERED (✗)"
  - Reason: Data corruption or incomplete copy/paste. Checksum failure.

 Hiccup B: "DATA NOISE / GARBAGE TEXT OUTPUT"
  - Reason: Incorrect Case-Sensitive Access Token.
    """ + RESET)

# ==========================================
# Input Mechanics & Idle Timer
# ==========================================
def get_menu_choice(prompt, timeout=120):
    if sys.platform == 'win32':
        try:
            import msvcrt
            sys.stdout.write(prompt)
            sys.stdout.flush()
            start_time = time.time()
            input_str = ""
            while True:
                if msvcrt.kbhit():
                    char = msvcrt.getwch()
                    if char in ('\x00', '\xe0'):
                        msvcrt.getwch()
                        continue
                    if char in ('\r', '\n'):
                        print()
                        return input_str
                    elif char == '\x08':
                        if len(input_str) > 0:
                            input_str = input_str[:-1]
                            sys.stdout.write('\b \b')
                            sys.stdout.flush()
                    elif char == '\x03':
                        raise KeyboardInterrupt
                    else:
                        input_str += char
                        sys.stdout.write(char)
                        sys.stdout.flush()
                if time.time() - start_time > timeout:
                    return None
                time.sleep(0.05)
        except Exception:
            return input(prompt).strip()
    else:
        try:
            import select
            sys.stdout.write(prompt)
            sys.stdout.flush()
            start_time = time.time()
            while True:
                ready, _, _ = select.select([sys.stdin], [], [], 0.1)
                if ready:
                    line = sys.stdin.readline()
                    if not line:
                        raise EOFError
                    return line.strip()
                if time.time() - start_time > timeout:
                    return None
        except Exception:
            return input(prompt).strip()

def get_multiline_input(prompt_text):
    print(prompt_text)
    commit_msg = "(Press Enter, then Ctrl+Z, then Enter)" if sys.platform.startswith('win') else "(Press Enter, then Ctrl+D)"
    print(GOLD + commit_msg + " [Type 'ABORT' to cancel]" + RESET)
    print(THEME_COLOR + BOLD + "> " + RESET, end="", flush=True)
    return sys.stdin.read().strip()

# ==========================================
# Main Control Loop
# ==========================================
def main():
    global OPERATOR_ALIAS, FAILED_ATTEMPTS
    
    run_cold_boot()
    clear_screen()
    print(THEME_COLOR + BOLD + "INITIALIZING VOID_DECK NEURAL LINK..." + RESET)
    time.sleep(0.5)
    
    OPERATOR_ALIAS = input(THEME_ACCENT + BOLD + "\nEnter Operator Handle (Alias): " + RESET).strip()
    if not OPERATOR_ALIAS:
        OPERATOR_ALIAS = "Guest"

    while True:
        print_header(MAIN_ART)
        print_random_quote()
        
        print(THEME_ACCENT + " [1] Generate Access Token (PRNG Seed)" + RESET)
        print(THEME_ACCENT + " [2] Upload to the Matrix (Encrypt Text)" + RESET)
        print(THEME_ACCENT + " [3] Jack Out of the Matrix (Decrypt Text)" + RESET)
        print(THEME_ACCENT + " [4] View Manual & Operational Guidelines" + RESET)
        print(THEME_ACCENT + " [5] Change Deck Color Interface Themes" + RESET)
        print(THEME_ACCENT + " [6] Initiate ESPER Voight-Kampff Bio-Scan" + RESET)
        print(GOLD + " [7] Black Box (Any-File Encrypt/Decrypt)" + RESET)
        print(THEME_ACCENT + " [8] Consult the Wintermute Oracle" + RESET)
        print(THEME_DARK + " [9] Enter Digital Rain (Matrix Idle State)" + RESET)
        print(PURPLE + " [S] Phantom Image Steganography" + RESET)
        print(PURPLE + " [Z] Zalgo Glitch-Text Corruptor" + RESET)
        print(RED + " [P] !!! PANIC PURGE !!! (Screen Self-Destruct)" + RESET)
        print(RED + " [0] Burn the Deck (Terminate Link)" + RESET)
        print(THEME_DARK + "─" * 65 + RESET)
        
        try: 
            choice = get_menu_choice(THEME_ACCENT + BOLD + "Select Deck Operation: " + RESET, timeout=120)
            if choice is None:
                digital_rain()
                continue
            choice = choice.strip().upper()
        except KeyboardInterrupt:
            continue
        except EOFError: 
            sys.exit(0)
            
        # ----------------------------------------
        # OPTION 1: GENERATE TOKEN
        # ----------------------------------------
        if choice == '1':
            print_header(KEY_ART)
            new_key = str(random.randint(100000000000, 999999999999))
            print(THEME_COLOR + "\nPolling atmospheric noise for unique entropy..." + RESET)
            time.sleep(0.7)
            print("\n" + THEME_ACCENT + "="*60)
            print("             !!! SECURE THIS ACCESS TOKEN !!!")
            print("="*60 + RESET)
            print(BOLD + CYAN + f"  {new_key}" + RESET)
            print(THEME_ACCENT + "="*60 + RESET)
            
        # ----------------------------------------
        # OPTION 2: ENCRYPT TEXT
        # ----------------------------------------
        elif choice == '2':
            print_header(CIPHER_ART)
            msg = get_multiline_input(THEME_COLOR + "Enter payload to upload to Matrix:" + RESET)
            
            if not sys.stdin.isatty():
                sys.stdin = open('/dev/tty')
                
            if not msg or msg.upper() == 'ABORT':
                print(RED + "[!] Matrix upload aborted." + RESET)
                time.sleep(1)
                continue

            key = getpass.getpass(THEME_COLOR + BOLD + "\nEnter Access Token (Hidden): " + RESET).strip()
            fast_mode_ans = input(THEME_ACCENT + BOLD + "SuperCiph (Fast Mode) [Y/N]: " + RESET).strip().upper()
            is_fast = True if fast_mode_ans == 'Y' else False
            
            random.seed(key)
            tagged = append_integrity_tag(msg, OPERATOR_ALIAS)
            cipher_bytes = bytearray(b ^ random.randint(0, 255) for b in tagged.encode('utf-8'))
            result_hex = cipher_bytes.hex()
            random.seed()
            
            print(THEME_ACCENT + "\n" + "="*65)
            print("SECURE DATAFRAME GENERATED:")
            print("="*65 + RESET)
            rolling_reveal_rainbow(result_hex, True, is_fast)
            print(THEME_ACCENT + "="*65 + RESET)
            
            if input(THEME_ACCENT + BOLD + "\nCyber-Jack to System Clipboard? [Y/N]: " + RESET).strip().upper() == 'Y':
                if copy_to_clipboard(result_hex):
                    print(GREEN + "[✓] Payload successfully injected to clipboard." + RESET)
                else:
                    print(RED + "[!] Clipboard injection failed (OS Not Supported)." + RESET)

            if input(THEME_ACCENT + BOLD + "Export to a local .DAT file? [Y/N]: " + RESET).strip().upper() == 'Y':
                filename = input(THEME_COLOR + "Enter filename (Blank for auto): " + RESET).strip()
                if not filename:
                    filename = f"MATRIX_DROP_{random.randint(1000, 9999)}.dat"
                if not filename.endswith('.dat'):
                    filename += ".dat"
                    
                try:
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(result_hex)
                    print(GREEN + BOLD + f"[✓] STEALTH DROP COMPLETE: Saved to {filename}" + RESET)
                except Exception as e:
                    print(RED + f"[!] Export Failed: {e}" + RESET)
                
        # ----------------------------------------
        # OPTION 3: DECRYPT TEXT
        # ----------------------------------------
        elif choice == '3':
            print_header(DECIPHER_ART)
            token_saved = ""
            is_fast_saved = False
            
            while True:
                cwd = os.getcwd()
                print(THEME_DARK + f"\n[ NODE_LOC ]: {cwd}" + RESET)
                print(THEME_COLOR + "Commands: (SCAN, SHIFT <dir>, LOC, CLIP, PASTE) or [TAB] to enter target .dat:" + RESET)
                nav_input = input(THEME_ACCENT + BOLD + "> " + RESET).strip()

                if nav_input.upper() == 'ABORT':
                    break
                    
                elif nav_input.upper() == 'SCAN':
                    print(THEME_DARK + "\nScanning directory sectors..." + RESET)
                    try:
                        for item in sorted(os.listdir('.')):
                            if item.lower().endswith('.dat'):
                                print(GOLD + f" [DAT_DROP] {item}" + RESET)
                            elif os.path.isdir(item):
                                print(CYAN + f" [DIR_NODE] {item}/" + RESET)
                            else:
                                print(THEME_DARK + f" [DATA_FRAG] {item}" + RESET)
                    except Exception as e:
                        print(RED + f"[!] Scan Error: {e}" + RESET)
                    continue
                    
                elif nav_input.upper().startswith('SHIFT '):
                    try:
                        os.chdir(nav_input[6:].strip())
                        print(GREEN + f"Shifted to node: {os.getcwd()}" + RESET)
                    except Exception as e:
                        print(RED + f"[!] Shift Error: {e}" + RESET)
                    continue
                    
                elif nav_input.upper() == 'LOC':
                    print(CYAN + f"Active Node: {os.getcwd()}" + RESET)
                    continue
                
                hex_payload = ""
                isfile_flag = False
                file_target = ""

                if nav_input.upper() == 'CLIP':
                    hex_payload = paste_from_clipboard()
                    if not hex_payload:
                        print(RED + "[!] Clipboard is empty or unreadable." + RESET)
                        continue
                    print(GREEN + "[✓] Cyber-Jack complete: Read from clipboard." + RESET)
                    
                elif nav_input.upper() == 'PASTE':
                    hex_payload = get_multiline_input(THEME_COLOR + "Input Raw HEX dataframe:" + RESET)
                    if not sys.stdin.isatty():
                        sys.stdin = open('/dev/tty')
                    if hex_payload.upper() == 'ABORT':
                        continue
                        
                elif os.path.isfile(nav_input):
                    try:
                        with open(nav_input, 'r', encoding='utf-8') as f:
                            hex_payload = f.read().strip()
                        print(GREEN + f"[✓] Dataframe loaded from {nav_input}" + RESET)
                        isfile_flag = True
                        file_target = nav_input
                    except Exception as e:
                        print(RED + f"[!] Read Error: {e}" + RESET)
                        continue
                else:
                    if all(c in string.hexdigits or c.isspace() for c in nav_input) and len(nav_input) > 4:
                        hex_payload = nav_input
                    else:
                        print(RED + "[!] Invalid command or file not found." + RESET)
                        continue

                if not token_saved:
                    token_saved = getpass.getpass(THEME_COLOR + BOLD + "Enter Access Token (Hidden): " + RESET).strip()
                    fast_mode_ans = input(THEME_ACCENT + BOLD + "SuperCiph (Fast Mode) [Y/N]: " + RESET).strip().upper()
                    is_fast_saved = True if fast_mode_ans == 'Y' else False

                # --- DURESS PROTOCOL CHECK ---
                if token_saved.lower() == 'cleansweep':
                    print(THEME_ACCENT + "\n" + "="*65)
                    print("JACKED OUT: DATA CONSTRUCT RECOVERED:")
                    print("="*65 + RESET)
                    rolling_reveal_rainbow(DURESS_DECOY, False, is_fast_saved)
                    print(THEME_ACCENT + "="*65 + RESET)
                    print(GREEN + BOLD + "[ GHOST_VERIFY: SECURE (✓) ] -- CONSTRUCT STABLE." + RESET)
                    
                    if isfile_flag:
                        if input(THEME_ACCENT + "Execute Burn Protocol (Secure Delete File)? [Y/N]: " + RESET).strip().upper() == 'Y':
                            try:
                                os.remove(file_target)
                                print(GREEN + "[✓] Source file securely shredded." + RESET)
                            except: pass

                    if input(THEME_COLOR + BOLD + "\nJack Out another dataframe with current Token? [Y/N]: " + RESET).strip().upper() != 'Y':
                        break
                    continue
                
                # --- STANDARD DECRYPTION ---
                random.seed(token_saved)
                try:
                    clean_hex = "".join(hex_payload.split())
                    cipher_bytes = list(bytes.fromhex(clean_hex))
                    plaintext = bytes([b ^ random.randint(0, 255) for b in cipher_bytes]).decode('utf-8')
                    random.seed()
                    
                    result_plain, verified, ts, alias = verify_and_strip_tag(plaintext)
                    
                    print(THEME_ACCENT + "\n" + "="*65)
                    print("JACKED OUT: DATA CONSTRUCT RECOVERED:")
                    print("="*65 + RESET)
                    rolling_reveal_rainbow(result_plain, False, is_fast_saved)
                    print(THEME_ACCENT + "="*65 + RESET)
                    
                    if verified:
                        print(GREEN + BOLD + "[ GHOST_VERIFY: SECURE (✓) ] -- CONSTRUCT STABLE." + RESET)
                        if ts:
                            print(CYAN + f"[ TIME_STAMP ]: Payload locked at {time.ctime(ts)}" + RESET)
                        if alias:
                            print(CYAN + f"[ OPERATOR ]: Message from <{alias}>" + RESET)
                        
                        if isfile_flag:
                            if input(THEME_ACCENT + "Execute Burn Protocol (Secure Delete File)? [Y/N]: " + RESET).strip().upper() == 'Y':
                                try:
                                    os.remove(file_target)
                                    print(GREEN + "[✓] Source file securely shredded." + RESET)
                                except Exception as e:
                                    print(RED + f"[!] Shred failed: {e}" + RESET)
                    else:
                        print(RED + BOLD + "[ GHOST_VERIFY: TAMPERED (✗) ] -- INTEGRITY COLLAPSE." + RESET)
                        FAILED_ATTEMPTS += 1
                        if check_black_ice():
                            break
                            
                except Exception as e:
                    print(RED + f"[!] ERROR: {e}" + RESET)
                    FAILED_ATTEMPTS += 1
                    if check_black_ice():
                        break

                if input(THEME_COLOR + BOLD + "\nJack Out another dataframe with current Token? [Y/N]: " + RESET).strip().upper() != 'Y':
                    break

        # ----------------------------------------
        # OPTION 4: MANUAL
        # ----------------------------------------
        elif choice == '4':
            display_manual()
            
        # ----------------------------------------
        # OPTION 5: THEME
        # ----------------------------------------
        elif choice == '5':
            print_header(MAIN_ART)
            print(THEME_ACCENT + " [1] Classic Matrix (Green)")
            print(" [2] Neon Tokyo (Pink)")
            print(" [3] ESPER Diagnostic (Amber)")
            print(" [4] Zion Resistance (Cyan)" + RESET)
            
            theme_choice = input(THEME_COLOR + BOLD + "\nSelect Deck Theme: " + RESET).strip()
            set_theme(theme_choice)
            
        # ----------------------------------------
        # OPTION 6: VOIGHT-KAMPFF
        # ----------------------------------------
        elif choice == '6':
            run_voight_kampff()
            
        # ----------------------------------------
        # OPTION 7: BLACK BOX (ANY FILE)
        # ----------------------------------------
        elif choice == '7':
            print_header(CIPHER_ART)
            print(THEME_ACCENT + "--- BLACK BOX ANY-FILE ENCRYPTOR ---" + RESET)
            print(GOLD + "Warning: This module processes raw binary (JPG, PDF, EXE)." + RESET)
            op = input(THEME_COLOR + BOLD + " [1] Encrypt File\n [2] Decrypt File\n > " + RESET).strip()
            
            if op in ['1', '2']:
                filepath = ""
                while True:
                    cwd = os.getcwd()
                    print(THEME_DARK + f"\n[ NODE_LOC ]: {cwd}" + RESET)
                    print(THEME_COLOR + "Commands: (SCAN, SHIFT <dir>, LOC) or [TAB] to enter target filename:" + RESET)
                    nav_input = input(THEME_ACCENT + BOLD + "> " + RESET).strip()
                    
                    if nav_input.upper() == 'ABORT':
                        break
                        
                    elif nav_input.upper() == 'SCAN':
                        print(THEME_DARK + "\nScanning directory sectors..." + RESET)
                        try:
                            for item in sorted(os.listdir('.')):
                                if item.lower().endswith('.ghost'):
                                    print(PURPLE + f" [GHOST_FILE] {item}" + RESET)
                                elif os.path.isdir(item):
                                    print(CYAN + f" [DIR_NODE] {item}/" + RESET)
                                else:
                                    print(THEME_DARK + f" [DATA_FRAG] {item}" + RESET)
                        except Exception as e:
                            print(RED + f"[!] Scan Error: {e}" + RESET)
                        continue
                        
                    elif nav_input.upper().startswith('SHIFT '):
                        try:
                            os.chdir(nav_input[6:].strip())
                            print(GREEN + f"Shifted to node: {os.getcwd()}" + RESET)
                        except Exception as e:
                            print(RED + f"[!] Shift Error: {e}" + RESET)
                        continue
                        
                    elif nav_input.upper() == 'LOC':
                        print(CYAN + f"Active Node: {os.getcwd()}" + RESET)
                        continue
                    
                    if os.path.isfile(nav_input):
                        filepath = nav_input
                        break
                    else:
                        print(RED + "[!] Invalid command or file not found." + RESET)
                
                if not filepath:
                    continue
                    
                key = getpass.getpass(THEME_COLOR + BOLD + "Enter Access Token (Hidden): " + RESET).strip()
                
                # --- DURESS CHECK FOR BINARY FILE ---
                if key.lower() == 'cleansweep' and op == '2':
                    out_path = filepath.replace(".ghost", "") + ".decrypted"
                    try:
                        with open(out_path, 'wb') as f:
                            f.write(DURESS_DECOY.encode('utf-8'))
                        print(GREEN + BOLD + "[✓] BINARY GHOST_VERIFY: SECURE. File restored." + RESET)
                        print(GREEN + f"Saved to: {out_path}" + RESET)
                        if input(THEME_ACCENT + "Execute Burn Protocol (Secure Delete Source)? [Y/N]: " + RESET).strip().upper() == 'Y':
                            os.remove(filepath)
                            print(GREEN + "[✓] Source file securely shredded." + RESET)
                    except Exception:
                        pass
                    continue
                
                try:
                    with open(filepath, 'rb') as f:
                        data = f.read()
                    
                    if op == '1':
                        crc_str = f"{zlib.crc32(data):08x}"
                        ts_str = f"{int(time.time()):08x}"
                        tag = f"###CRC:{crc_str}:{ts_str}:{OPERATOR_ALIAS}###".encode('utf-8')
                        payload = data + tag
                        
                        random.seed(key)
                        enc_data = bytearray(b ^ random.randint(0, 255) for b in payload)
                        random.seed()
                        
                        out_path = filepath + ".ghost"
                        with open(out_path, 'wb') as f:
                            f.write(enc_data)
                        print(GREEN + BOLD + f"[✓] File Encrypted and saved to: {out_path}" + RESET)
                        
                    elif op == '2':
                        random.seed(key)
                        dec_data = bytearray(b ^ random.randint(0, 255) for b in data)
                        random.seed()
                        
                        clean_data, verified, ts_ext, alias_ext = verify_binary_tag(dec_data)
                        
                        if verified:
                            out_path = filepath.replace(".ghost", "")
                            if out_path == filepath:
                                out_path += ".decrypted"
                            with open(out_path, 'wb') as f:
                                f.write(clean_data)
                            print(GREEN + BOLD + "[✓] BINARY GHOST_VERIFY: SECURE. File restored." + RESET)
                            if ts_ext:
                                print(CYAN + f"[ TIME_STAMP ]: File locked at {time.ctime(ts_ext)}" + RESET)
                            if alias_ext:
                                print(CYAN + f"[ OPERATOR ]: File encoded by <{alias_ext}>" + RESET)
                            print(GREEN + f"Saved to: {out_path}" + RESET)
                            
                            if input(THEME_ACCENT + "Execute Burn Protocol (Secure Delete Source)? [Y/N]: " + RESET).strip().upper() == 'Y':
                                try:
                                    os.remove(filepath)
                                    print(GREEN + "[✓] Source file securely shredded." + RESET)
                                except Exception as e:
                                    print(RED + f"[!] Shred failed: {e}" + RESET)
                        else:
                            print(RED + "[✗] INTEGRITY COLLAPSE. Incorrect Key or corrupted file." + RESET)
                            FAILED_ATTEMPTS += 1
                            check_black_ice()
                            
                except Exception as e:
                    print(RED + f"[!] Process Error: {e}" + RESET)

        # ----------------------------------------
        # OPTION 8: ORACLE
        # ----------------------------------------
        elif choice == '8':
            consult_oracle()
            
        # ----------------------------------------
        # OPTION 9: DIGITAL RAIN
        # ----------------------------------------
        elif choice == '9':
            digital_rain()
        
        # ----------------------------------------
        # OPTION S: PHANTOM STEGANOGRAPHY
        # ----------------------------------------
        elif choice == 'S':
            print_header(CIPHER_ART)
            print(THEME_ACCENT + "--- PHANTOM IMAGE STEGANOGRAPHY ---" + RESET)
            print(GOLD + "Hides encrypted HEX invisibly at the end of .jpg or .png files." + RESET)
            op = input(THEME_COLOR + BOLD + " [1] Inject Payload into Image\n [2] Extract Payload from Image\n > " + RESET).strip()
            
            if op == '1':
                img_path = input(THEME_COLOR + "Enter target image path: " + RESET).strip()
                if not os.path.isfile(img_path):
                    print(RED + "[!] File not found." + RESET)
                    continue
                
                msg = get_multiline_input(THEME_COLOR + "Enter payload to hide:" + RESET)
                if not sys.stdin.isatty():
                    sys.stdin = open('/dev/tty')
                if not msg or msg.upper() == 'ABORT':
                    continue
                
                key = getpass.getpass(THEME_COLOR + BOLD + "Enter Access Token (Hidden): " + RESET).strip()
                
                random.seed(key)
                tagged = append_integrity_tag(msg, OPERATOR_ALIAS)
                cipher_bytes = bytearray(b ^ random.randint(0, 255) for b in tagged.encode('utf-8'))
                result_hex = cipher_bytes.hex()
                random.seed()
                
                try:
                    with open(img_path, 'ab') as f:
                        f.write(b"\n###PHANTOM###" + result_hex.encode('utf-8') + b"###PHANTOM###")
                    print(GREEN + BOLD + "[✓] Payload successfully injected into image matrix." + RESET)
                except Exception as e:
                    print(RED + f"[!] Injection Error: {e}" + RESET)
                
            elif op == '2':
                img_path = input(THEME_COLOR + "Enter carrier image path: " + RESET).strip()
                if not os.path.isfile(img_path):
                    print(RED + "[!] File not found." + RESET)
                    continue
                
                key = getpass.getpass(THEME_COLOR + BOLD + "Enter Access Token (Hidden): " + RESET).strip()
                fast = input(THEME_ACCENT + BOLD + "SuperCiph [Y/N]: " + RESET).strip().upper() == 'Y'
                
                # --- DURESS PROTOCOL ---
                if key.lower() == 'cleansweep':
                    print(THEME_ACCENT + "\n" + "="*65)
                    print("JACKED OUT: DATA CONSTRUCT RECOVERED:")
                    print("="*65 + RESET)
                    rolling_reveal_rainbow(DURESS_DECOY, False, fast)
                    print(THEME_ACCENT + "="*65 + RESET)
                    print(GREEN + BOLD + "[ GHOST_VERIFY: SECURE (✓) ] -- CONSTRUCT STABLE." + RESET)
                    continue

                try:
                    with open(img_path, 'rb') as f:
                        content = f.read()
                        
                    idx1 = content.rfind(b"###PHANTOM###")
                    if idx1 == -1:
                        print(RED + "[!] No phantom signature found in file." + RESET)
                        continue
                    
                    idx0 = content.rfind(b"###PHANTOM###", 0, idx1-1)
                    if idx0 == -1:
                        print(RED + "[!] Corrupted phantom signature." + RESET)
                        continue
                    
                    hex_payload = content[idx0+13:idx1].decode('utf-8')
                    
                    random.seed(key)
                    cipher_bytes = list(bytes.fromhex(hex_payload))
                    plaintext = bytes([b ^ random.randint(0, 255) for b in cipher_bytes]).decode('utf-8')
                    random.seed()
                    
                    result_plain, verified, ts, alias = verify_and_strip_tag(plaintext)
                    
                    print(THEME_ACCENT + "\n" + "="*65)
                    print("JACKED OUT: DATA CONSTRUCT RECOVERED:")
                    print("="*65 + RESET)
                    rolling_reveal_rainbow(result_plain, False, fast)
                    print(THEME_ACCENT + "="*65 + RESET)
                    
                    if verified:
                        print(GREEN + BOLD + "[ GHOST_VERIFY: SECURE (✓) ]" + RESET)
                        if ts:
                            print(CYAN + f"[ TIME_STAMP ]: Payload locked at {time.ctime(ts)}" + RESET)
                        if alias:
                            print(CYAN + f"[ OPERATOR ]: Message from <{alias}>" + RESET)
                        
                        if input(THEME_ACCENT + "Execute Burn Protocol (Secure Delete Image)? [Y/N]: " + RESET).strip().upper() == 'Y':
                            os.remove(img_path)
                            print(GREEN + "[✓] Carrier file shredded." + RESET)
                    else:
                        print(RED + BOLD + "[ GHOST_VERIFY: TAMPERED (✗) ]" + RESET)
                        
                except Exception as e:
                    print(RED + f"[!] Extraction Error: {e}" + RESET)
                
        # ----------------------------------------
        # OPTION Z: ZALGO CORRUPTOR
        # ----------------------------------------
        elif choice == 'Z':
            print_header(MAIN_ART)
            print(BOLD + PURPLE + "--- ZALGO GLITCH-TEXT CORRUPTOR ---" + RESET)
            text = input(THEME_COLOR + "Enter baseline text to corrupt: " + RESET).strip()
            if text:
                out = generate_zalgo(text)
                print(THEME_ACCENT + "\n" + "="*65 + RESET)
                print(out)
                print(THEME_ACCENT + "="*65 + RESET)
                if input(THEME_ACCENT + "\nCopy to clipboard? [Y/N]: " + RESET).strip().upper() == 'Y':
                    if copy_to_clipboard(out):
                        print(GREEN + "[✓] Glitch copied to system clipboard." + RESET)
            
        # ----------------------------------------
        # OPTION P: PANIC PURGE
        # ----------------------------------------
        elif choice == 'P': 
            run_panic_purge()
            continue
            
        # ----------------------------------------
        # OPTION 0: QUIT
        # ----------------------------------------
        elif choice == '0':
            print(RED + f"\nDisconnecting Deck interface. See you later, {OPERATOR_ALIAS}." + RESET)
            time.sleep(0.5)
            clear_screen()
            sys.exit(0)
            
        else:
            print(RED + "\n[!] UNRECOGNIZED CONSOLE QUERY." + RESET)
            
        input(THEME_DARK + "\nPress Enter to reload VOID_DECK..." + RESET)

if __name__ == "__main__":
    main()
