import styled from "vue3-styled-components";

export const BackgroundTextWrapper = styled.div`
  // Need to hide the source text to display it repeated as a background.
  height: 0;
  overflow: hidden;
  
  .text {
    text-align: center;
    font-size: 50px;
    font-weight: 900;
    color: black;

    span {
      color: hotpink;
    }
  }
`;