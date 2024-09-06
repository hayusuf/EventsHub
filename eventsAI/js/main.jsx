import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import Post from "./post";

// Create a root
const root = createRoot(document.getElementById("reactEntry"));

root.render(
  <StrictMode>
    <Post url="/api/question" />
  </StrictMode>
);
