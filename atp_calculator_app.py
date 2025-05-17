import streamlit as st

def calculate_atp_details(glucose_molecules):
    results = {}

    # 해당과정
    glycolysis_atp_direct = 2 * glucose_molecules  # 기질수준 인산화
    glycolysis_nadh = 2 * glucose_molecules        # 산화적 인산화

    # 피루브산 산화
    pyruvate_nadh = 2 * glucose_molecules

    # TCA 회로
    tca_nadh = 6 * glucose_molecules
    tca_fadh2 = 2 * glucose_molecules
    tca_atp_direct = 2 * glucose_molecules         # 기질수준 인산화

    # 산화적 인산화 계산
    nadh_to_atp = (glycolysis_nadh + pyruvate_nadh + tca_nadh) * 2.5
    fadh2_to_atp = tca_fadh2 * 1.5
    substrate_level_atp = glycolysis_atp_direct + tca_atp_direct
    total_atp = nadh_to_atp + fadh2_to_atp + substrate_level_atp

    results['기질수준 인산화'] = {
        "해당과정 직접 생성": glycolysis_atp_direct,
        "TCA 회로 직접 생성": tca_atp_direct,
        "총합": substrate_level_atp
    }

    results['산화적 인산화'] = {
        "해당과정 NADH (2×2.5)": glycolysis_nadh * 2.5,
        "피루브산 산화 NADH (2×2.5)": pyruvate_nadh * 2.5,
        "TCA 회로 NADH (6×2.5)": tca_nadh * 2.5,
        "TCA 회로 FADH₂ (2×1.5)": fadh2_to_atp,
        "총합": nadh_to_atp + fadh2_to_atp
    }

    results['총 ATP 생성량'] = total_atp
    return results

# Streamlit UI
st.title("세포호흡 ATP 계산기 🧬🔬")
st.markdown("""
**산화적 인산화**와 **기질수준 인산화**를 구분하여  
세포호흡 단계별 ATP 생성량을 자세히 계산합니다.
""")

glucose = st.number_input("포도당 분자 수 입력:", min_value=1, step=1, value=1)

if st.button("ATP 생성량 계산"):
    result = calculate_atp_details(glucose)

    st.header("📌 기질수준 인산화 ATP")
    for k, v in result['기질수준 인산화'].items():
        if k != '총합':
            st.write(f"- {k}: {v} ATP")
    st.write(f"**총합: {result['기질수준 인산화']['총합']} ATP**")

    st.header("📌 산화적 인산화 ATP")
    for k, v in result['산화적 인산화'].items():
        if k != '총합':
            st.write(f"- {k}: {v:.2f} ATP")
    st.write(f"**총합: {result['산화적 인산화']['총합']:.2f} ATP**")

    st.markdown("---")
    st.success(f"🌟 총 ATP 생성량: **{result['총 ATP 생성량']:.2f} ATP**")
