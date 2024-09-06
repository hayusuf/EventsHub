import React, { useState } from "react";
import PropTypes from "prop-types";

export default function Post({ url }) {
  const [prompt, setPrompt] = useState("");
  const [previousAnswers, setPreviousAnswers] = useState([]);
  const [currentAnswer, setCurrentAnswer] = useState("");

  const handlePromptChange = (e) => {
    setPrompt(e.target.value);
  };

  const handleFetchData = () => {
    // Call REST API to get the post's information using the provided prompt
    fetch(`${url}?prompt=${encodeURIComponent(prompt)}`, {
      credentials: "same-origin",
    })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        setCurrentAnswer(data.answer);
        setPreviousAnswers((prevAnswers) => [...prevAnswers, data.answer]);
      })
      .catch((error) => console.log(error));
  };

  return (
    <div>
      <label>
        Enter your prompt:
        <input type="text" value={prompt} onChange={handlePromptChange} />
      </label>
      <button onClick={handleFetchData}>Fetch Data</button>
      <h1>Current Response: {currentAnswer}</h1>
      <div className="previous-answers-container">
        <h2>Previous Answers:</h2>
        <ul>
          {previousAnswers.map((answer, index) => (
            <li key={index}>{answer}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

Post.propTypes = {
  url: PropTypes.string.isRequired,
};
