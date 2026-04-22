import qrcode

print("=== UPI QR Generator (All Apps Supported) ===")

phone = input("Enter Phone Number (optional): ")
upi_id = input("Enter UPI ID (optional): ")
name = input("Enter Receiver Name: ")
amount = input("Enter Amount (optional): ")

# Decide payment ID
if upi_id:
    pay_id = upi_id
elif phone:
    pay_id = phone + "@upi"
else:
    print("❌ Enter at least Phone Number or UPI ID")
    exit()

# Create universal UPI URL
upi_url = f"upi://pay?pa={pay_id}&pn={name}&am={amount}&cu=INR"

# Generate QR
qr = qrcode.make(upi_url)

# Save & show
qr.save("upi_all_apps_qr.png")
qr.show()

print("✅ One QR works in all UPI apps!")
