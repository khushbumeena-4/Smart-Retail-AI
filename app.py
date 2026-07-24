import streamlit as st
import cv2
from PIL import Image
import numpy as np
from ultralytics import YOLO

from database import (
    get_product,
    update_quantity,
    get_all_products
)

from receipt import generate_receipt


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Smart Retail AI",
    page_icon="🛒",
    layout="wide"
)


# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main {
    background-color:#0e1117;
}


h1 {
    color:#00ff99;
    text-align:center;
}


h2,h3 {
    color:#ffffff;
}


.card {

    background:#1c1f26;

    padding:20px;

    border-radius:15px;

    border:1px solid #333;

}


.stButton button {

    width:100%;

    background:#00ff99;

    color:black;

    font-weight:bold;

    border-radius:10px;

}


</style>

""",unsafe_allow_html=True)



# -----------------------------
# LOAD MODEL
# -----------------------------

@st.cache_resource
def load_model():

    return YOLO("yolov8n.pt")


model = load_model()



# -----------------------------
# SESSION
# -----------------------------

if "cart" not in st.session_state:

    st.session_state.cart={}



# -----------------------------
# HEADER
# -----------------------------

st.markdown(
"""
<h1>
🛒 Smart Retail AI Checkout
</h1>

<p style='text-align:center;color:#aaa'>
YOLOv8 + OpenCV + Inventory Automation
</p>

""",
unsafe_allow_html=True
)


st.divider()



# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("⚙️ Control Panel")


page = st.sidebar.radio(

    "Select Module",

    [
        "📷 AI Scanner",
        "💳 Billing",
        "📦 Inventory"
    ]

)


st.sidebar.divider()


st.sidebar.info(
"""
System Status

🟢 Camera Ready

🟢 YOLO Loaded

🟢 Database Connected
"""
)



# ====================================================
# CAMERA MODULE
# ====================================================


if page=="📷 AI Scanner":


    st.header("📷 Product Scanner")


    col1,col2 = st.columns([2,1])


    with col1:


        camera = st.camera_input(
            "Capture Product Image"
        )


    with col2:


        st.markdown(
        """
        <div class="card">

        ### How to use

        1. Place products in front of camera

        2. Capture image

        3. Run AI Detection

        4. Checkout

        </div>

        """,
        unsafe_allow_html=True
        )



    if camera:


        image = Image.open(camera)

        frame=np.array(image)



        if st.button(
            "🚀 Run Detection"
        ):


            results=model(frame)


            detected={}


            output=frame.copy()



            for result in results:


                for box in result.boxes:


                    conf=float(box.conf[0])


                    if conf<0.5:
                        continue


                    cls=int(box.cls[0])


                    name=model.names[cls]


                    detected[name]=(
                        detected.get(name,0)+1
                    )



                    x1,y1,x2,y2=map(
                        int,
                        box.xyxy[0]
                    )


                    cv2.rectangle(
                        output,
                        (x1,y1),
                        (x2,y2),
                        (0,255,0),
                        3
                    )


                    cv2.putText(
                        output,
                        name,
                        (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        .8,
                        (0,255,0),
                        2
                    )



            st.image(
                output,
                caption="AI Detection Result",
                width=700
            )



            st.session_state.cart=detected



            st.success(
                "Products Added To Cart"
            )




    if st.session_state.cart:


        st.subheader("🛒 Current Cart")


        cart_data=[]


        for k,v in st.session_state.cart.items():

            cart_data.append(
                {
                    "Product":k,
                    "Quantity":v
                }
            )


        st.table(cart_data)




# ====================================================
# BILLING
# ====================================================


elif page=="💳 Billing":


    st.header("💳 Smart Billing")


    if not st.session_state.cart:


        st.warning(
            "Cart empty. Scan products first."
        )


    else:


        total=0

        bill=[]


        for item,qty in st.session_state.cart.items():


            product=get_product(item)


            if product:


                _,name,price,stock=product


                amount=price*qty


                total+=amount


                bill.append(
                {
                "Product":name,
                "Quantity":qty,
                "Price":price,
                "Amount":amount
                })



        st.table(bill)



        st.metric(
            "Total Payable",
            f"₹ {total}"
        )



        if st.button(
            "✅ Confirm Payment"
        ):


            for item in st.session_state.cart:

                update_quantity(
                    item,
                    st.session_state.cart[item]
                )


            pdf=generate_receipt(
                bill,
                total
            )


            st.success(
                "Payment Completed"
            )


            with open(pdf,"rb") as f:

                st.download_button(
                    "📄 Download Receipt",
                    f,
                    file_name="receipt.pdf"
                )




# ====================================================
# INVENTORY
# ====================================================


elif page=="📦 Inventory":


    st.header(
        "📦 Inventory Dashboard"
    )


    products=get_all_products()


    st.dataframe(
        products,
        width=800
    )