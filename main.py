from pyscript import document

def compute_average(event):
    # Get the input values and convert to float
    input1 = float(document.getElementById("input1").value)
    input2 = float(document.getElementById("input2").value)

    # Compute average
    average = (input1 + input2) / 2

    # Determine pass/fail
    if average >= 85:
        result = "Yes"
    else:
        result = "No"

    # Display results
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result
