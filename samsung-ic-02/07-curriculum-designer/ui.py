import streamlit as st

from ai_backend import generate_curriculum

st.set_page_config(
    page_title="Curriculum Builder",
    layout="wide",
)

st.title("📚 AI Curriculum Builder")

subject = st.text_input(
    "Subject",
    value="AI Mastery",
)

domain_context = st.text_area(
    "Learning Domain Context",
    value="Software engineers with Python knowledge who want to become AI engineers.",
)

time_budget = st.text_input(
    "Time Budget",
    value="6 months",
)

generate = st.button("Generate Curriculum")

if generate:

    if not subject.strip():
        st.error("Please enter a subject.")
        st.stop()

    with st.spinner("Generating Curriculum..."):

        try:

            curriculum = generate_curriculum(
                subject,
                domain_context,
                time_budget,
            )

        except Exception as e:
            st.exception(e)
            st.stop()

    st.title(curriculum["course_title"])

    st.write(curriculum["summary"])

    st.subheader("Target Audience")

    st.write(curriculum["target_audience"])

    st.subheader("Prerequisites")

    for item in curriculum["prerequisites"]:
        st.write("•", item)

    st.subheader("Learning Outcomes")

    for item in curriculum["learning_outcomes"]:
        st.write("•", item)

    st.subheader("Recommended Tools")

    for tool in curriculum["tools"]:
        st.write("•", tool)

    st.divider()

    st.header("Modules")

    for module in curriculum["modules"]:

        with st.expander(
            f"Module {module['module_number']} - {module['module_title']}",
            expanded=False,
        ):

            st.markdown(
                f"**Learning Outcome**\n\n{module['learning_outcome']}"
            )

            st.markdown("### Topics")

            for topic in module["topics"]:
                st.write("•", topic)

            st.success(
                f"Mini Project: {module['mini_project']}"
            )

            st.markdown("### Execution Plan")

            plan = module["execution_plan"]

            st.write("**Duration:**", plan["duration"])

            st.markdown("#### Activities")

            for activity in plan["activities"]:
                st.write("•", activity)

            st.markdown("#### Deliverables")

            for deliverable in plan["deliverables"]:
                st.write("•", deliverable)

    st.divider()

    st.header("Final Capstone")

    capstone = curriculum["final_capstone"]

    st.subheader(capstone["title"])

    st.write(capstone["description"])

    st.markdown("### Skills Covered")

    for skill in capstone["skills_covered"]:
        st.write("•", skill)