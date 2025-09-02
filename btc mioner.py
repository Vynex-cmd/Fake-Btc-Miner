import tkinter as tk
import random
import threading
import time

# Globals
btc_mined = 0.0
mining = True

def fake_mining_log():
    templates = [
        "New job received: diff {diff}",
        "Hashrate: {hashrate} MH/s",
        "Accepted share: nonce {nonce}, diff {diff}",
        "Rejected share: nonce {nonce}, stale job",
        "Block found! Reward credited: 0.000125 BTC",
        "Connecting to stratum server...",
        "Verifying proof of work...",
        "Submitted share - OK",
        "GPU {gpu_id} temperature: {temp}°C",
        "Switching to backup pool..."
    ]
    return random.choice(templates).format(
        diff=round(random.uniform(500, 5000), 2),
        hashrate=round(random.uniform(20, 100), 2),
        nonce=random.randint(100000, 999999),
        gpu_id=random.randint(0, 3),
        temp=random.randint(50, 80)
    )

def update_logs(text_widget):
    while mining:
        log = fake_mining_log()
        text_widget.insert(tk.END, log + '\n')
        text_widget.see(tk.END)
        time.sleep(random.uniform(0.1, 0.4))  # Faster mining logs

def update_btc_counter(label):
    global btc_mined
    while mining:
        increment = random.uniform(0.000001, 0.00001)
        btc_mined += increment
        label.config(text=f"BTC Mined: {btc_mined:.8f}")
        time.sleep(0.5)

def start_fake_miner():
    miner_window = tk.Toplevel()
    miner_window.title("BTC Miner")
    miner_window.geometry("700x500")

    title = tk.Label(miner_window, text="Bitcoin Miner", font=("Helvetica", 14, "bold"))
    title.pack(pady=5)

    btc_label = tk.Label(miner_window, text="BTC Mined: 0.00000000", font=("Courier", 12), fg="yellow")
    btc_label.pack(pady=5)

    text_widget = tk.Text(miner_window, bg="black", fg="lime", insertbackground="white", font=("Courier", 10))
    text_widget.pack(fill=tk.BOTH, expand=True)

    threading.Thread(target=update_logs, args=(text_widget,), daemon=True).start()
    threading.Thread(target=update_btc_counter, args=(btc_label,), daemon=True).start()

# Main launcher window
root = tk.Tk()
root.title("Crypto Tool")
root.geometry("300x150")

label = tk.Label(root, text="Click to Start BTC Mining", font=("Arial", 12))
label.pack(pady=20)

start_button = tk.Button(root, text="Start Miner", command=start_fake_miner, bg="green", fg="white")
start_button.pack()

root.mainloop()
