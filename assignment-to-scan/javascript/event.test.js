/** @jest-environment jsdom */

const { eventHandler } = require("./event");

// Mock table to store data into //
document.body.innerHTML = 
    `<table>
        <thead>
          <th>Event Name</th>
          <th>Representative's Name</th>
          <th>Representative's Email</th>
          <th>Representative's Role</th>
          <th>Event Cancellation</th>
        </thead>
        <tbody id="tbody">
        </tbody>
    </table>`

test("eventHandler successfully adds the example event to the table and event list", () => {

    // Example input //
    let example_event_name = "Example Event"
    let example_rep_name = "Example Rep Name"
    let example_email = "email@email.com"
    let example_role = "Example Role"

   const mock_table = document.getElementById("tbody")

    global.table = mock_table

    eventHandler(example_event_name, example_rep_name, 
                        example_email, example_role)

    const row = mock_table.children[0];
    expect(row.children[0].innerText).toBe(example_event_name);
    expect(row.children[1].innerText).toBe(example_rep_name);
    expect(row.children[2].innerText).toBe(example_email);
    expect(row.children[3].innerText).toBe(example_role);
})