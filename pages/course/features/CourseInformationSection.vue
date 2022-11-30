<template>
  <section id="course-information">
    <div class="course-information__content">
      <div class="course-information-content__left">
        <h1>WEB DEVELOPMENT<br />BOOTCAMP</h1>
        <h4>
          Ready for a change? Become a professional Web Developer and boost your career or launch your own
          business.
        </h4>
        <p>
          <strong>Start</strong> April 17th 2023 <br />
          <strong>Duration</strong> 12 weeks (+4 weeks online preparation) <br />
          <strong>Times</strong> 5 days/week, 9am - 6pm <br />
          <strong>Price</strong> $13,999 (payment plans available) <br />
          <strong>Program</strong> Fullstack (Frontend & Backend) <br />
          <strong>Technologies</strong>
          HTML, CSS, JavaScript, React, Node.js, Next.js, GraphQL, PostgreSQL, GitHub and many more <br />
          <strong>Experience</strong> no upfront coding knowledge needed <br />
        </p>
        <h4>
          Do you have questions? <br />
          Let's talk! Click the link below to schedule time with us.
        </h4>
        <CoreButton size="L" variant="secondary">
          Schedule A Meeting
        </CoreButton>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
#course-information {
  display: flex;
  justify-content: center;
  height: 60vh;
  padding: 5rem 5%;
  border-radius: 3rem;
  background-color: var(--white);

  .course-information__content {
    display: grid;
    align-items: center;
    flex: 1;
    max-width: 144rem;
    background-color: var(--white);
    grid-template-columns: 1fr 1fr;

    .course-information-content__left {
      font-size: 1.728rem;
      display: flex;
      flex-direction: column;
      gap: 5rem;

      h1 {
        font-size: 7.2rem;
        line-height: 72.19%;
        color: var(--white);
        text-shadow: 8px 8px 0 var(--black);
        -webkit-text-stroke: 3px var(--black);
      }

      button {
        margin-right: auto;
      }
    }
  }
}
</style>