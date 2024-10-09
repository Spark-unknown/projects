from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


def generate_receipt():
    company_name = input("Enter company name: ")
    company_address = input("Enter company address: ")
    company_phone = input("Enter company phone number: ")
    company_email = input("Enter company email: ")

    customer_name = input("Enter customer name: ")
    invoice_number = input("Enter invoice number: ")
    date = input("Enter date (DD/MM/YYYY): ")

    num_items = int(input("Enter number of items purchased: "))
    items = []
    for i in range(num_items):
        item_name = input(f"Enter item {i+1} name: ")
        item_price = input(f"Enter item {i+1} price: ")
        item_quantity = input(f"Enter item {i+1} quantity: ")
        items.append([item_name, item_price, item_quantity])

    subtotal = sum(float(item[1]) * float(item[2]) for item in items)
    tax_rate = 0.08  
    tax = subtotal * tax_rate
    total = subtotal + tax

    DATA = [
        ["Date", "Invoice Number", "Customer Name"],
        [date, invoice_number, customer_name],
        ["", "", ""],
        ["Item", "Price", "Quantity", "Total"],
    ]
    for item in items:
        DATA.append([item[0], item[1], item[2], f"${float(item[1]) * float(item[2]):.2f}"])
    DATA.append(["", "", "", ""])
    DATA.append(["Subtotal", "", "", f"${subtotal:.2f}"])
    DATA.append(["Tax (8%)", "", "", f"${tax:.2f}"])
    DATA.append(["Total", "", "", f"${total:.2f}"])

    pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.alignment = 1

    company_details = f"{company_name}\n{company_address}\n{company_phone}\n{company_email}"
    company_paragraph = Paragraph(company_details, styles["Normal"])

    receipt_title = f"Receipt for {customer_name}"
    receipt_title_paragraph = Paragraph(receipt_title, title_style)

    style = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (4, 4), 1, colors.black),
            ("BACKGROUND", (0, 0), (3, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )

    table = Table(DATA, style=style)

    try:
        with open('receipt.pdf', 'wb') as f:
            pdf.build([company_paragraph, receipt_title_paragraph, table])
        print("Receipt generated successfully!")
    except Exception as e:
        print(f"Error generating receipt: {str(e)}")


if __name__ == "__main__":
    generate_receipt()