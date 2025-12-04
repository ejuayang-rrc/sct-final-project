// JavaScript Document

// Volunteer Tracker Script
// Author: Elijah Juayang

const form = document.getElementById("volunteer-hours-tracker");

window.addEventListener("DOMContentLoaded", () => {
  displayScores();
});

// --------------- Submit Button Event Listener ---------------

/**
 * Event Listener when "Register" button (button with "submit" as type) in form is clicked.
 * The purpose of this function is to collect values from the Form's inputs and store them in variables.
 * Then validate each given input.  
 */
form.addEventListener("submit", (event) => 
  { 
  event.preventDefault();
  
  const success = document.getElementById("submittedMsg");
  success.classList.remove("display-error");
  clearErrors();
  
  let validity = true;
  
  // ---- Validation ---- 
  
  const inputs = form.elements;
  
  const name = inputs["name"];
  const nameValue = name.value;
  
  if ( nameValue === null ||  nameValue === "" ) {
    showErrorMsg("name", "Input must be a Full Name.");
    showErrorVisual("name");
    validity = false;
  }
  
  const numbers = inputs["numbers"];
  const numbersValue = numbers.value;
  
  if ( numbersValue === null ||  numbersValue === "" ) {
    showErrorMsg("numbers", "Please input hours volunteered.");
    showErrorVisual("numbers");
    validity = false;
  } 
  else if ( numbersValue < 0 ) {
    showErrorMsg("numbers", "Invalid hours.");
    showErrorVisual("numbers");
    validity = false;
  }
  
  const date = inputs["date"];
  const dateValue = date.value;
  
  if ( dateValue === null ||  dateValue === "" ) {
    showErrorMsg("date", "Please select a date.");
    showErrorVisual("date");
    validity = false;
  }
  
  const rate = inputs["rate"];
  const rateValue = Number(rate.value);
  
  if ( rateValue === null ||  rateValue === "" ) {
    showErrorMsg("rate", "Please give a rating.");
    showErrorVisual("rate");
    validity = false;
  } 
  else if ( rateValue > 5 ||  rateValue < 1 ) {
    showErrorMsg("rate", "Please give a rating between 1 and 5.");
    showErrorVisual("rate");
    validity = false;
  } 
  
  // Display if form is properly filled with valid data.
  if ( validity === true ) {
    saveVolunteer(nameValue, numbersValue, dateValue, rateValue);
    displayScores();
    success.classList.add("display-error");
  }
});

// --------------- Storage Management ---------------

/**
 * Saves a volunteer with a unique ID.
 * @param {string} charityName - The name of the charity.
 * @param {number} loggedHours, - The hour's volunteered.
 * @param {string} dateVolunteered - The volunteer date.
 * @param {number} experienceRating - The volunteer's rating.
 */
function saveVolunteer(charityName, loggedHours, dateVolunteered, experienceRating) {
  const volunteers = JSON.parse(localStorage.getItem("volunteers")) || [];
  
  var idNumber = 1;
  
  // Booleans and loop to verify if ID is unique.
  var isUnique = false;
  
  while (!isUnique) {
    let loopAgain = false;
    
    volunteers.forEach(row => {
      if (idNumber == row.id) {
        idNumber += 1;
        loopAgain = true;
      }
    });
    
    if (!loopAgain) {
      isUnique = true;
    }
  }

  // Add new volunteer to array.
  volunteers.push(
    { 
      id: idNumber, 
      name: charityName, 
      hours: loggedHours, 
      date: dateVolunteered, 
      rating: experienceRating 
    }
  );

  localStorage.setItem("volunteers", JSON.stringify(volunteers));
}

/**
 * Displays volunteers to the Volunteer Hours Tracker table.
 */
function displayScores() 
{
  const tableBody = document.getElementById("volunteer-table").querySelector("tbody");
  tableBody.innerHTML = "";

  const volunteers = JSON.parse(localStorage.getItem("volunteers")) || [];
  
  if (volunteers.length === 0) {
    document.getElementById("volunteer-table").classList.add("hidden");
  } else {
    document.getElementById("volunteer-table").classList.remove("hidden");
  }
  
  console.log(volunteers);

  volunteers.forEach(row => {
    let tableRow = document.createElement("tr");
    
    let rowName = document.createElement("td");
    rowName.innerText = row.name;
    let rowHours = document.createElement("td");
    rowHours.innerText = row.hours;
    let rowDate = document.createElement("td");
    rowDate.innerText = row.date;
    
    let rowRating = document.createElement("td");
    rowRating.className = "table-rating";
    let rating = row.rating;
    let stars = "";
    
    while (rating > 0) {
      stars += '\u{f005}';
      rating -= 1;
    }
    
    rowRating.innerText = stars;
    
    let deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete";
    deleteButton.addEventListener("click", function() {
      tableRow.remove();
      
      let data = JSON.parse(localStorage.getItem("volunteers")) || [];
      let updatedData = data.filter(entry => entry.id !== row.id);
      localStorage.setItem("volunteers", JSON.stringify(updatedData));
      
      if (updatedData.length === 0) {
        document.getElementById("volunteer-table").classList.add("hidden");
      } else {
        document.getElementById("volunteer-table").classList.remove("hidden");
      }
    });
    
    tableRow.appendChild(rowName);
    tableRow.appendChild(rowHours);
    tableRow.appendChild(rowDate);
    tableRow.appendChild(rowRating);
    tableRow.appendChild(deleteButton);
    tableBody.appendChild(tableRow);
  });
}

// --------------- Error Display ---------------

/**
 * Shows error to specified field with message.
 */
const showErrorMsg = (fieldName, message) => 
{
  const errorFieldId = `${fieldName}Error`;
	const errorField = document.getElementById(errorFieldId);
  
  if (!errorField) 
  {
		console.error(`Error with ID '${errorFieldId}' field not found.`);
		return;
	}
  
  errorField.textContent = message;
  errorField.classList.add("display-error");
}

/**
 * Shows error to specified field with visual.
 */
const showErrorVisual = (fieldName) => 
{
  const errorInputId = `${fieldName}Input`;
	const errorInput = document.getElementById(errorInputId);
  
  if (!errorInput) 
  {
		console.error(`Error with ID '${errorInputId}' input element not found.`);
		return;
	}
  
  errorInput.classList.add("error-highlight");
}

/**
 * Clears all errors throughout the Form.
 */
const clearErrors = () => 
{
	const errorMessage = document.querySelectorAll(".error-msg");
  const highlightedField = document.querySelectorAll(".error-highlight");
  
	errorMessage.forEach((errorField) => 
  {
    errorField.textContent = "";
		errorField.classList.remove("display-error");
	});
  
  highlightedField.forEach((inputField) => 
  {
    inputField.classList.remove("error-highlight");
  });
};
