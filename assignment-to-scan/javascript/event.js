// JavaScript Document

function verifyEvent(event){
    event.preventDefault()
    let form_completed = true
  
    //Section to reset error messages.//
  
    document.getElementById("event_name_error").textContent = "";
    document.getElementById("rep_name_error").textContent = "";
    document.getElementById("email_error").textContent = "";
    document.getElementById("role_error").textContent = "";
  
    //Section for selecting values of the inputs.//
  
    let event_name = document.getElementById("event_name").value;
    let rep_name = document.getElementById("rep_name").value;
    let email = document.getElementById("email").value;
    let role = document.getElementById("role").value;

    //Section for checking if form meets proper requirements.//
  
    if (event_name === ""){
      document.getElementById("event_name_error").textContent = "A name for the event is REQUIRED.";
          form_completed = false;
    }
  
    if (rep_name === ""){
      document.getElementById("rep_name_error").textContent = "The name of the representative is REQUIRED.";
          form_completed = false;
    }
  
    if (email === ""){
      document.getElementById("email_error").textContent = "The email of the representative is REQUIRED.";
          form_completed = false;
    }
    
    if (role === "no_role"){
      document.getElementById("role_error").textContent = "The role being taken is REQUIRED.";
          form_completed = false;
    }
  
    if (form_completed === true){
        // Sends the verified information to the handler. //
      eventHandler(event_name, rep_name, email, role);
    }}
  
  // The eventHandler takes the verified information given from the
  // verify event function and processes it into the localStorageItem "events",
  // re-saves the Item and alls the tableUpdate method.

  function eventHandler(event_name, rep_name, email, role) {
    const event_list = updateEvents();
    event_list.push({event_name, rep_name, email, role});
    saveEvents(event_list);
    tableUpdate();
  }

  // This function takes the localStorageItem "events" and using the JSON.parse function
  // converts the item into an array to be sorted through when making the table section.

  function updateEvents(){
   const event_list = localStorage.getItem("events");
   return event_list ? JSON.parse(event_list) : [];
  }

  // Saves over pre-existing version of the localStorageItem "events" with the most
  // updated version of the event_list.

  function saveEvents(event_list){
    localStorage.setItem("events", JSON.stringify(event_list));
  }

  // Removes an event from the event_list array and updates
  // the localStorageItem "events"
  
  function removeEvent(row_position){
    const event_list = updateEvents();
    event_list.splice(row_position, 1);
    saveEvents(event_list);
    tableUpdate();
    alert("The event has been cancelled.");
  }

  //Updates the table using the current localStorageItem "events" using
  // a converted version of it as an array. It creates a new element for each
  // event (EV) in the array. It also displays a message when no event's are found.

  function tableUpdate() {
    const tbody = document.getElementById("tbody");
    tbody.innerHTML = "";
    const no_events = document.getElementById("no_event");
    no_events.innerHTML = "";

    const event_list = updateEvents();

    event_list.forEach((EV, row_position) => {
        let row = document.createElement("tr")

        row.innerHTML = `
        <td>${EV.event_name}</td>
        <td>${EV.rep_name}</td>
        <td>${EV.email}</td>
        <td>${EV.role}</td>
        <td><button onclick="removeEvent(${row_position})">Cancel Event</button></td>
        `
        tbody.appendChild(row);
    });

    if (event_list.length === 0) {
        no_events.innerHTML = "There are currently no ongoing events.";
    }}

// Initial run of tableUpdate() on page load.
  tableUpdate();

// Runs a unit test //
  module.exports = { eventHandler };