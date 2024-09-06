import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";

export default function Question({ url }) {
  const [q, setQ] = useState("");

  useEffect(() => {
    // Declare a boolean flag that we can use to cancel the API request.
    let ignoreStaleRequest = false;

    // Call REST API to get the post's information
    fetch(url, { credentials: "same-origin" })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        // If ignoreStaleRequest was set to true, we want to ignore the results of the
        // the request. Otherwise, update the state to trigger a new render.

        if (!ignoreStaleRequest) {
          // Assuming data.q is the property you want to display
          setQ(data.q || "hello");
        }
      })
      .catch((error) => console.log(error));

    return () => {
      // This is a cleanup function that runs whenever the Question component
      // unmounts or re-renders. If a Question is about to unmount or re-render, we
      // should avoid updating state.
      ignoreStaleRequest = true;
    };
  }, [url]);

  return <p>look here: {q}</p>;
}

Question.propTypes = {
  url: PropTypes.string.isRequired,
};
