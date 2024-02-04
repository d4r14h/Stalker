import wmi

c = wmi.WMI()

updates = c.Win32_QuickFixEngineering(Description="Security Update")

latest_update = sorted(updates, key=lambda u: u.InstallDate, reverse=True)[0]

print("Latest Windows update:")
print("- HotFixID:", latest_update.HotFixID)
print("- Description:", latest_update.Description)
print("- Installed on:", latest_update.InstallDate)
