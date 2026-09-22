import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="KAU 2022 Agriculture Batch Analytics",
    page_icon="🌾",
    layout="wide"
)

# -----------------------------
# KAU 2022 B.Sc. (Hons.) Ag.
# College of Agriculture, Vellanikkara
# -----------------------------
DATA = [
[1,"2022-41-301","AARCHA T J","FEMALE",8.58],
[2,"2022-41-302","AARDRA C S","FEMALE",7.67],
[3,"2022-41-303","ABDULLAH BIN SHAMSUDHEEN","MALE",7.96],
[4,"2022-41-304","ADITHYA N","FEMALE",8.91],
[5,"2022-41-305","AKSHAY RAJAN","MALE",8.71],
[6,"2022-41-306","ALEENA JOSEPH","FEMALE",8.28],
[7,"2022-41-307","ALEENA JOY","FEMALE",9.04],
[8,"2022-41-309","AMRUTHESWARY M S","FEMALE",8.40],
[9,"2022-41-310","ANAMIKA K","FEMALE",8.32],
[10,"2022-41-311","ANAMIKA V","FEMALE",7.01],
[11,"2022-41-312","ANANYA KRISHNA S","FEMALE",7.88],
[12,"2022-41-313","ANASWARA ANAND P","FEMALE",8.10],
[13,"2022-41-314","ANCHIMA AJITHKUMAR","FEMALE",8.67],
[14,"2022-41-315","ANILA M S","FEMALE",8.83],
[15,"2022-41-316","ANILA P RAJU","FEMALE",9.01],
[16,"2022-41-317","ANJALI SASI","FEMALE",7.73],
[17,"2022-41-318","ANJALY K K","FEMALE",8.28],
[18,"2022-41-319","ANJANA K S","FEMALE",8.36],
[19,"2022-41-320","ANJANA P M","FEMALE",8.73],
[20,"2022-41-321","ANJANA UNNI","FEMALE",8.39],
[21,"2022-41-322","ANN CATHERIEN","FEMALE",8.63],
[22,"2022-41-323","ANNA P JACOB","FEMALE",6.28],
[23,"2022-41-324","ANSIYA T N","FEMALE",8.16],
[24,"2022-41-325","ANU P SUNIL","FEMALE",8.63],
[25,"2022-41-326","ANUPAMA ANILKUMAR","FEMALE",8.07],
[26,"2022-41-327","ARJUN BUBESH","MALE",7.37],
[27,"2022-41-328","ARYA S","FEMALE",8.92],
[28,"2022-41-329","ARYA P","FEMALE",8.89],
[29,"2022-41-330","ARYA S","FEMALE",8.56],
[30,"2022-41-331","ASNA SHERIN","FEMALE",8.04],
[31,"2022-41-332","ASWAYA N S","FEMALE",8.37],
[32,"2022-41-333","ATHIRA SURESH","FEMALE",9.14],
[33,"2022-41-334","ATHULKRISHNA K S","MALE",7.83],
[34,"2022-41-335","AVANTHIKA A","FEMALE",9.04],
[35,"2022-41-336","AVANTHIKA RISHIKESH","FEMALE",6.32],
[36,"2022-41-337","AVANTHIKA S","FEMALE",8.31],
[37,"2022-41-338","AYISHATH SAHLA","FEMALE",8.55],
[38,"2022-41-339","AYSHA ABIJA M T","FEMALE",8.14],
[39,"2022-41-340","BIJESH V P","MALE",7.70],
[40,"2022-41-341","BINHA CHEMMANOR BRIJI","FEMALE",8.48],
[41,"2022-41-342","BINSA B","FEMALE",8.42],
[42,"2022-41-344","CHANDANA M","FEMALE",7.93],
[43,"2022-41-345","CHIDANAND A","MALE",8.15],
[44,"2022-41-346","DEVIKA KRISHNAN K","FEMALE",8.77],
[45,"2022-41-347","DILSHA K","FEMALE",8.97],
[46,"2022-41-348","DIVYA S","FEMALE",8.39],
[47,"2022-41-349","DIYA P","FEMALE",8.85],
[48,"2022-41-350","DIYA SAJEESH BABU","FEMALE",8.93],
[49,"2022-41-351","FATHIMA FASNA P","FEMALE",8.77],
[50,"2022-41-352","FATHIMA MISRIYYA E T","FEMALE",7.83],
[51,"2022-41-353","FATHIMA NOURIN P B","FEMALE",9.01],
[52,"2022-41-354","FATHIMATH RAHNA M P","FEMALE",8.54],
[53,"2022-41-355","FIDA JEBIN P K","FEMALE",8.14],
[54,"2022-41-356","GALIB AHRAS AMEEN C P","MALE",7.21],
[55,"2022-41-357","GANGA K","FEMALE",7.98],
[56,"2022-41-358","GANGA NAIR","FEMALE",9.20],
[57,"2022-41-359","HADIY","MALE",6.52],
[58,"2022-41-360","HARIPRIYA M","FEMALE",9.06],
[59,"2022-41-361","HARSHA A","FEMALE",8.42],
[60,"2022-41-363","HIBA S PARVEEN","FEMALE",7.49],
[61,"2022-41-364","INSHA SAHEER","FEMALE",8.06],
[62,"2022-41-365","JAGINA J M","FEMALE",8.91],
[63,"2022-41-366","JAYALEKSHMI S","FEMALE",8.75],
[64,"2022-41-367","LAKSHMI K C","FEMALE",8.84],
[65,"2022-41-368","LEENA P","FEMALE",8.25],
[66,"2022-41-369","MARY MERLIN K P","FEMALE",8.89],
[67,"2022-41-370","MEENU MATHEW","FEMALE",8.75],
[68,"2022-41-371","MEKHA SAJI","FEMALE",7.60],
[69,"2022-41-372","MILOOFA M BASHEER","FEMALE",8.23],
[70,"2022-41-373","MINZIYA NAZEER","FEMALE",8.53],
[71,"2022-41-374","MOHAMED FAYIZ M P","MALE",8.96],
[72,"2022-41-375","MOHAMMED ANSHIF K M","MALE",8.20],
[73,"2022-41-376","NADHIYA A K","FEMALE",8.16],
[74,"2022-41-377","NAJAH KANNIYAN","FEMALE",8.75],
[75,"2022-41-378","NANDANA T J","FEMALE",9.05],
[76,"2022-41-379","NAVYA PREMDAS","FEMALE",7.70],
[77,"2022-41-380","NIDHINA M","FEMALE",8.72],
[78,"2022-41-381","NIHAL I","MALE",7.71],
[79,"2022-41-382","NIHMA KV","FEMALE",8.03],
[80,"2022-41-383","P T MUHAMMED SALAH","MALE",7.62],
[81,"2022-41-384","PARVATHI PR","FEMALE",7.58],
[82,"2022-41-385","PIVIN MOSA M","MALE",7.41],
[83,"2022-41-386","PRIYAMVADA K M","FEMALE",8.93],
[84,"2022-41-387","PUNNYA SANTHOSH T","FEMALE",8.08],
[85,"2022-41-388","RAJALAKSHMI MS","FEMALE",7.82],
[86,"2022-41-389","RAKENDHU REMESH","FEMALE",8.68],
[87,"2022-41-392","SANJANA T","FEMALE",8.42],
[88,"2022-41-393","SANTHWANA SANTHOSH","FEMALE",8.97],
[89,"2022-41-394","SHARLET SANTHOSH","FEMALE",8.63],
[90,"2022-41-395","SHIBLA M","FEMALE",7.92],
[91,"2022-41-397","SIDHARTH A","MALE",8.12],
[92,"2022-41-398","SIJIYA K J","FEMALE",8.19],
[93,"2022-41-399","SINDRIA S S","FEMALE",9.14],
[94,"2022-41-400","SIVANANDANA M ANIL","FEMALE",8.40],
[95,"2022-41-401","SNEHA MARY JOYCHEN","FEMALE",8.55],
[96,"2022-41-402","SNEHA P G","FEMALE",8.50],
[97,"2022-41-403","SONA N","FEMALE",8.82],
[98,"2022-41-404","SREELAKSHMI S","FEMALE",8.51],
[99,"2022-41-405","SREELAKSHMI S MENON","FEMALE",8.26],
[100,"2022-41-406","SREEPRABHA K","FEMALE",8.32],
[101,"2022-41-407","THEERTHA KRISHNA","FEMALE",8.04],
[102,"2022-41-408","UTHARA S","FEMALE",9.23],
[103,"2022-41-409","VARSHA","FEMALE",8.63],
[104,"2022-41-411","VISMAYA S","FEMALE",7.91],
]

df = pd.DataFrame(DATA, columns=["Sl No","Admission No","Name","Gender","OGPA"])

# Rank: competition ranking, equal OGPAs receive same rank
df["Rank"] = df["OGPA"].rank(method="min", ascending=False).astype(int)
df = df.sort_values(["Rank", "Name"]).reset_index(drop=True)

# -----------------------------
# Header
# -----------------------------
st.title("🌾 KAU 2022 Agriculture Batch Analytics")
st.caption("B.Sc. (Hons.) Agriculture — College of Agriculture, Vellanikkara")

st.info(
    "This dashboard uses the final OGPA list of the 2022 admission batch. "
    "OGPA is out of 10.00."
)

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("🔎 Filters")

gender_options = ["All"] + sorted(df["Gender"].unique().tolist())
selected_gender = st.sidebar.selectbox("Gender", gender_options)

min_gpa = float(df["OGPA"].min())
max_gpa = float(df["OGPA"].max())

gpa_range = st.sidebar.slider(
    "OGPA range",
    min_value=5.0,
    max_value=10.0,
    value=(min_gpa, max_gpa),
    step=0.01
)

search = st.sidebar.text_input("Search student name")

filtered = df.copy()

if selected_gender != "All":
    filtered = filtered[filtered["Gender"] == selected_gender]

filtered = filtered[
    (filtered["OGPA"] >= gpa_range[0]) &
    (filtered["OGPA"] <= gpa_range[1])
]

if search.strip():
    filtered = filtered[
        filtered["Name"].str.contains(search.strip(), case=False, na=False)
    ]

# -----------------------------
# KPI cards
# -----------------------------
c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Students", len(filtered))
c2.metric("Average OGPA", f"{filtered['OGPA'].mean():.2f}" if len(filtered) else "—")
c3.metric("Median OGPA", f"{filtered['OGPA'].median():.2f}" if len(filtered) else "—")
c4.metric("Highest OGPA", f"{filtered['OGPA'].max():.2f}" if len(filtered) else "—")
c5.metric("Lowest OGPA", f"{filtered['OGPA'].min():.2f}" if len(filtered) else "—")

st.divider()

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["📊 Dashboard", "🏆 Ranking", "👤 Student Search", "📋 Full Data"]
)

with tab1:
    if len(filtered) == 0:
        st.warning("No students match the selected filters.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            fig = px.histogram(
                filtered,
                x="OGPA",
                nbins=15,
                title="OGPA Distribution",
                labels={"OGPA": "Final OGPA", "count": "Students"}
            )
            fig.update_layout(bargap=0.08)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            gender_counts = filtered["Gender"].value_counts().reset_index()
            gender_counts.columns = ["Gender", "Students"]

            fig2 = px.pie(
                gender_counts,
                names="Gender",
                values="Students",
                title="Gender Distribution",
                hole=0.45
            )
            st.plotly_chart(fig2, use_container_width=True)

        # GPA bands
        st.subheader("📚 OGPA Bands")

        bins = [0, 6, 7, 8, 8.5, 9, 9.5, 10.01]
        labels = [
            "< 6.00",
            "6.00–6.99",
            "7.00–7.99",
            "8.00–8.49",
            "8.50–8.99",
            "9.00–9.49",
            "9.50–10.00"
        ]

        band_df = filtered.copy()
        band_df["OGPA Band"] = pd.cut(
            band_df["OGPA"],
            bins=bins,
            labels=labels,
            right=False
        )

        bands = band_df["OGPA Band"].value_counts().sort_index().reset_index()
        bands.columns = ["OGPA Band", "Students"]

        fig3 = px.bar(
            bands,
            x="OGPA Band",
            y="Students",
            title="Students by OGPA Band",
            text="Students"
        )
        fig3.update_traces(textposition="outside")
        st.plotly_chart(fig3, use_container_width=True)

        # Gender averages
        st.subheader("👥 Average OGPA by Gender")

        gender_avg = (
            filtered.groupby("Gender", as_index=False)["OGPA"]
            .mean()
            .round(3)
        )

        fig4 = px.bar(
            gender_avg,
            x="Gender",
            y="OGPA",
            title="Average OGPA by Gender",
            text="OGPA"
        )
        fig4.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        fig4.update_yaxes(range=[0, 10])
        st.plotly_chart(fig4, use_container_width=True)

with tab2:
    st.subheader("🏆 Batch Ranking")

    ranking = filtered[
        ["Rank", "Name", "Gender", "Admission No", "OGPA"]
    ].sort_values(["Rank", "Name"])

    st.dataframe(
        ranking,
        use_container_width=True,
        hide_index=True,
        column_config={
            "OGPA": st.column_config.NumberColumn(
                "OGPA",
                format="%.2f"
            ),
            "Rank": st.column_config.NumberColumn("Rank")
        }
    )

    st.subheader("🥇 Top 10")

    top10 = filtered.sort_values(
        ["OGPA", "Name"], ascending=[False, True]
    ).head(10).copy()

    top10["Position"] = range(1, len(top10) + 1)

    st.dataframe(
        top10[
            ["Position", "Name", "Gender", "OGPA", "Admission No"]
        ],
        use_container_width=True,
        hide_index=True
    )

with tab3:
    st.subheader("👤 Individual Student Profile")

    names = sorted(df["Name"].tolist())

    selected_student = st.selectbox(
        "Select a student",
        names
    )

    student = df[df["Name"] == selected_student].iloc[0]

    a, b, c, d = st.columns(4)

    a.metric("Rank", int(student["Rank"]))
    b.metric("OGPA", f"{student['OGPA']:.2f}")
    c.metric("Gender", student["Gender"])
    d.metric("Batch", "2022")

    st.write("### Student Details")

    details = pd.DataFrame({
        "Field": [
            "Name",
            "Admission Number",
            "Gender",
            "Final OGPA",
            "Batch Rank"
        ],
        "Value": [
            student["Name"],
            student["Admission No"],
            student["Gender"],
            f"{student['OGPA']:.2f}",
            int(student["Rank"])
        ]
    })

    st.table(details)

    # Position relative to batch
    percentile = (
        (df["OGPA"] < student["OGPA"]).sum() / len(df) * 100
    )

    st.metric(
        "Percentage of batch below this OGPA",
        f"{percentile:.1f}%"
    )

with tab4:
    st.subheader("📋 Complete Student Dataset")

    display_df = filtered[
        ["Rank", "Sl No", "Admission No", "Name", "Gender", "OGPA"]
    ].sort_values(["Rank", "Name"])

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "OGPA": st.column_config.NumberColumn(
                "Final OGPA",
                format="%.2f"
            )
        }
    )

    csv = display_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Filtered Data as CSV",
        data=csv,
        file_name="KAU_2022_Batch_Analytics.csv",
        mime="text/csv"
    )

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "Data source: KAU final result notification for 2022 admission B.Sc. (Hons.) Agriculture batch. "
    "For academic exploration only."
)
