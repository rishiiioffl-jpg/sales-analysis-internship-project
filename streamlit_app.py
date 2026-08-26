import streamlit as st
import requests
import pandas as pd


# ==========================================
# CONFIGURATION
# ==========================================

API_URL = "https://sales-analysis-api-deef.onrender.com"


st.set_page_config(
    page_title="Sales Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fb;
    }

    .title {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #6b7280;
        font-size: 18px;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# API HELPER
# ==========================================

def get_api_data(endpoint):

    try:

        response = requests.get(
            f"{API_URL}{endpoint}",
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:

        st.error(
            f"Unable to connect to API: {error}"
        )

        return None


# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="title">📊 E-Commerce Sales Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Sales analysis powered by FastAPI and Streamlit</div>',
    unsafe_allow_html=True
)


# ==========================================
# API STATUS
# ==========================================

try:
    response = requests.get(
        f"{API_URL}/",
        timeout=60
    )

    if response.status_code == 200:
        st.success("🟢 API Connected")
    else:
        st.warning(
            f"🟡 API responded with status {response.status_code}"
        )

except requests.exceptions.RequestException as error:
    st.error(f"🔴 API Offline: {error}")


# ==========================================
# LOAD SUMMARY
# ==========================================

summary = get_api_data(
    "/sales/summary"
)


if summary:

    # ======================================
    # KEY METRICS
    # ======================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "💰 Total Revenue",
            f"₹{summary['total_revenue']:,.2f}"
        )

    with col2:

        st.metric(
            "📈 Average Sale",
            f"₹{summary['average_sale']:,.2f}"
        )

    with col3:

        st.metric(
            "📦 Quantity Sold",
            f"{summary['total_quantity_sold']:,}"
        )

    with col4:

        st.metric(
            "🏆 Best Product",
            summary["best_selling_product"]
        )


    st.divider()


    # ======================================
    # ADDITIONAL INSIGHTS
    # ======================================

    st.subheader("🔎 Key Insights")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.write("**Highest Sale**")

        st.write(
            f"₹{summary['highest_sale']:,.2f}"
        )

    with col2:

        st.write("**Lowest Sale**")

        st.write(
            f"₹{summary['lowest_sale']:,.2f}"
        )

    with col3:

        st.write("**Best Sales Day**")

        st.write(
            summary["best_sales_day"]
        )

    with col4:

        st.write("**Best Product Revenue**")

        st.write(
            f"₹{summary['best_product_sales']:,.2f}"
        )


    st.divider()


    # ======================================
    # PRODUCT & CATEGORY ANALYSIS
    # ======================================

    col1, col2 = st.columns(2)


    # PRODUCT SALES

    with col1:

        st.subheader("🛍️ Product-wise Sales")

        product_data = get_api_data(
            "/sales/products"
        )

        if product_data:

            product_df = pd.DataFrame(
                list(product_data.items()),
                columns=[
                    "Product",
                    "Sales"
                ]
            )

            product_df = product_df.sort_values(
                "Sales",
                ascending=False
            )

            st.bar_chart(
                product_df.set_index("Product")
            )

            st.dataframe(
                product_df,
                use_container_width=True,
                hide_index=True
            )


    # CATEGORY SALES

    with col2:

        st.subheader("📂 Category-wise Sales")

        category_data = get_api_data(
            "/sales/categories"
        )

        if category_data:

            category_df = pd.DataFrame(
                list(category_data.items()),
                columns=[
                    "Category",
                    "Sales"
                ]
            )

            category_df = category_df.sort_values(
                "Sales",
                ascending=False
            )

            st.bar_chart(
                category_df.set_index("Category")
            )

            st.dataframe(
                category_df,
                use_container_width=True,
                hide_index=True
            )


    st.divider()


    # ======================================
    # DAILY SALES
    # ======================================

    st.subheader("📅 Daily Sales Trend")

    daily_data = get_api_data(
        "/sales/daily"
    )

    if daily_data:

        daily_df = pd.DataFrame(
            list(daily_data.items()),
            columns=[
                "Date",
                "Sales"
            ]
        )

        daily_df["Date"] = pd.to_datetime(
            daily_df["Date"]
        )

        daily_df = daily_df.sort_values(
            "Date"
        )

        daily_df = daily_df.set_index(
            "Date"
        )

        st.line_chart(
            daily_df["Sales"]
        )


    st.divider()


    # ======================================
    # MONTHLY SALES
    # ======================================

    st.subheader("📆 Monthly Sales Trend")

    monthly_data = get_api_data(
        "/sales/monthly"
    )

    if monthly_data:

        monthly_df = pd.DataFrame(
            list(monthly_data.items()),
            columns=[
                "Month",
                "Sales"
            ]
        )

        monthly_df = monthly_df.sort_values(
            "Month"
        )

        monthly_df = monthly_df.set_index(
            "Month"
        )

        st.bar_chart(
            monthly_df["Sales"]
        )


    st.divider()


    # ======================================
    # COMPLETE SUMMARY
    # ======================================

    with st.expander(
        "📋 View Complete Sales Summary"
    ):

        st.json(summary)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("📊 Sales Analysis")

    st.markdown(
        """
        ### Dashboard Features

        - 💰 Revenue Analysis
        - 🛍️ Product Analysis
        - 📂 Category Analysis
        - 📅 Daily Trends
        - 📆 Monthly Trends
        - 🏆 Best Product
        - 📈 Sales Insights
        - 🔌 FastAPI Integration
        """
    )

    st.divider()

    st.markdown(
        "**Backend API**"
    )

    st.code(API_URL)

    st.link_button(
        "Open API Documentation",
        f"{API_URL}/docs"
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "E-Commerce Sales Analysis Project • "
    "Built with Python, Pandas, FastAPI & Streamlit"
)