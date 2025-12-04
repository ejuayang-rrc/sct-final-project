/** @jest-environment jsdom */

const { loadDonationData } = require("./donations.js");

document.body.innerHTML = `<table id="donation_table"></table>`;

test("loadDonationData adds a row to the table", () => {
  const donation = {
    id: Math.floor((Math.random() * 10)+1),
    charity: "Larry Society",
    amount: "1000",
    date: "2025-03-29",
    comment: "Yeah"
  };

  const table = document.getElementById("donation_table");

  loadDonationData(donation);

  expect(table.children.length).toBe(1);

  const row = table.children[0];
  expect(row.children[0].innerText).toBe(donation.id);
  expect(row.children[1].innerText).toBe(donation.charity);
  expect(row.children[2].innerText).toBe(`$${donation.amount}`);
  expect(row.children[3].innerText).toBe(donation.date);
  expect(row.children[4].innerText).toBe(donation.comment);

  const deleteButton = row.children[5].querySelector("button");
  expect(deleteButton).not.toBeNull();
  expect(deleteButton.innerText).toBe("Delete");
});