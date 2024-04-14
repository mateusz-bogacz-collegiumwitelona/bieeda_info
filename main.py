from Gui import SystemInfoApp

if __name__ == "__main__":
    try:
        app = SystemInfoApp()
        app.mainloop()
    except KeyboardInterrupt:
        print("Ctrl+C detected. Exiting gracefully...")
