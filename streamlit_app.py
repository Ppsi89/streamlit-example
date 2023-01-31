import streamlit as st

# Page 1: Introduction and main contribution
st.title("Multipage Summary")
st.write("This is a multipage summary of a Python code project.")
st.write("The following pages will cover the main contribution, model changes, results, and fitting processes.")

# Page 2: Model changes
def model_changes():
    st.write("Model Changes")
    changed = st.checkbox("Have you changed the model since the last iteration?")
    if changed:
        st.write("Details of the changes made to the model:")
        st.write("[insert details here]")
    else:
        st.write("The model has not been changed since the last iteration.")

# Page 3: Results and benchmark comparison
def results_and_comparison():
    st.write("Results and Benchmark Comparison")
    st.write("Results obtained:")
    st.write("[insert results here]")
    st.write("Comparison with benchmark:")
    st.write("[insert comparison here]")

# Page 4: Goals and fitting processes
def goals_and_fitting_processes():
    st.write("Goals and Fitting Processes")
    st.write("For each of the project's goals, detail how they were achieved or not:")
    st.write("[insert details here]")
    st.write("In which process(es) can your model fit?")
    st.write("[insert fitting process details here]")

# Page 5: Conclusion
def conclusion():
    st.write("Conclusion")
    st.write("[insert conclusion here]")

# Main menu
def main():
    st.write("Main Menu")
    menu = ["Introduction and Main Contribution", "Model Changes", "Results and Benchmark Comparison", "Goals and Fitting Processes", "Conclusion"]
    choice = st.sidebar.selectbox("Select a page:", menu)

    if choice == "Introduction and Main Contribution":
        st.write("Main Contribution:")
        st.write("[insert main contribution details here]")

    elif choice == "Model Changes":
        model_changes()

    elif choice == "Results and Benchmark Comparison":
        results_and_comparison()

    elif choice == "Goals and Fitting Processes":
        goals_and_fitting_processes()

    elif choice == "Conclusion":
        conclusion()

if __name__ == '__main__':
    main()
