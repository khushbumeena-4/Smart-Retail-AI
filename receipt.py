from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from datetime import datetime
import os


def generate_receipt(bill, grand_total):

    os.makedirs("receipts", exist_ok=True)

    filename = f"receipts/Receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("<b>SMART RETAIL CHECKOUT</b>", styles["Title"])
    elements.append(title)

    elements.append(
        Paragraph(
            datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            styles["Normal"]
        )
    )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    data = [["Product", "Qty", "Price", "Total"]]

    for item in bill:
        data.append([
            item["name"],
            item["quantity"],
            f"₹{item['price']}",
            f"₹{item['total']}"
        ])

    data.append(["", "", "Grand Total", f"₹{grand_total}"])

    table = Table(data, colWidths=[2*inch, 1*inch, 1*inch, 1*inch])

    table.setStyle(TableStyle([

        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BACKGROUND",(0,1),(-1,-2),colors.beige),

        ("BACKGROUND",(-2,-1),(-1,-1),colors.lightgrey),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("BOTTOMPADDING",(0,0),(-1,0),10),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

    ]))

    elements.append(table)

    elements.append(Paragraph("<br/><br/>Thank You For Shopping!", styles["Heading2"]))

    doc.build(elements)

    print(f"Receipt Saved : {filename}")

    return filename