const form = document.createElement("form");
form.setAttribute("charset", "UTF-8");
form.setAttribute("method", "post");
form.setAttribute("action", "");

const input = document.createElement("input");
input.setAttribute("type", "hidden");
input.setAttribute("name", "");
input.setAttribute("value", "");

form.appendChild(input);

document.body.appendChild(form);
form.submit();



const createFormOneElement = () => {};
const createFormManyElement = () => {};
