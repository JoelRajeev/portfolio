function calculateDays()
{
    let dob = document.getElementById("dob").value;

    if(dob === "")
    {
        document.getElementById("result").innerText = "Please select date of birth";
        return;
    }

    let birthDate = new Date(dob);
    let today = new Date();

    let diffTime = today - birthDate;

    let daysAlive = Math.floor(diffTime / (1000 * 60 * 60 * 24));

    document.getElementById("result").innerText =
        "You have lived for " + daysAlive + " days";
}