(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
// JavaScript Document

// Element legend
const donation_prompt = document.getElementById("donation_prompt");
const table = document.getElementById("donation_table");

donation_prompt.classList.add("hidden");

function addDonation()
{
    donation_prompt.classList.remove("hidden");
}

// Processes the donation information to be loaded and added
function processData()
{
  donation_prompt.classList.add("hidden");

  // Date.now() looked like a good substitute
  var id_number = Math.floor((Math.random() * 10)+1);
    console.log(id_number);
  let charity_name = document.getElementById('charity_name').value;
    console.log(charity_name);
  let donation_amount = document.getElementById('donation_amount').value;
    console.log(donation_amount);
  let date_of_donation = document.getElementById('date_of_donation').value;
    console.log(date_of_donation);
  let donor_comment = document.getElementById('donor_comment').value;

  if (charity_name == "" || 
      donation_amount == "" || 
      date_of_donation == "yyyy-mm-dd")
      {
        alert("Please enter proper values");
        return false;
      }

  // Change this to store these items into a collection or JSON
  var donation_information = {
    id: id_number,
    charity: charity_name,
    amount: donation_amount,
    date: date_of_donation,
    comment: donor_comment
  }

  let donation = JSON.parse(localStorage.getItem("donation")) || [];
  donation.push(donation_information);
  localStorage.setItem("donation", JSON.stringify(donation));
  console.log(localStorage.getItem("donation"));

  loadDonationData(donation_information)
}

// Processes the rows to be added
// This needed to be added for persistence
function loadDonationData(row)
{
  var tr = document.createElement("tr");
  console.log(tr);

  var td1 = document.createElement("td");
    td1.innerText = row.id;
    console.log(td1);
  var td2 = document.createElement("td");
    td2.innerText = row.charity;
    console.log(td2);
  var td3 = document.createElement("td");
    td3.innerText = "$" + row.amount;
    console.log(td3);
  var td4 = document.createElement("td");
    td4.innerText = row.date;
    console.log(td4);
  var td5 = document.createElement("td");
    td5.innerText = row.comment;
    console.log(td5);
  var td6 = document.createElement("td");
    console.log(td6);

  // Delete button functionality
  var deleteButton = document.createElement("button");
  deleteButton.className = "delete_button";
  deleteButton.innerText = "Delete";
  deleteButton.addEventListener("click", function() {
    tr.remove();
  
  // This will delete the localStorage item
  let data = JSON.parse(localStorage.getItem("donation")) || [];
  let updatedData = data.filter(entry => entry.id !== row.id);
  localStorage.setItem("donation", JSON.stringify(updatedData));
  });

  td6.appendChild(deleteButton);

  // Appends the loaded data to a row
  tr.appendChild(td1);
  tr.appendChild(td2);
  tr.appendChild(td3);
  tr.appendChild(td4);
  tr.appendChild(td5);
  tr.appendChild(td6);

  // Outputs a row
  table.appendChild(tr);
}

window.addEventListener("DOMContentLoaded", () => {
  let donations = JSON.parse(localStorage.getItem("donation")) || [];
  donations.forEach(donations => {
    loadDonationData(donations)
  });
});

},{}]},{},[1]);
