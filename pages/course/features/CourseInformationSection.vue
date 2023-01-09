<template>
  <section id="course-information">
    <div class="course-information__content">
      <div class="course-information-content__left">
        <h1>WEB DEVELOPMENT<br/>BOOTCAMP</h1>
        <h4>
          Ready for a change? Become a professional Web Developer and boost your career or launch your own
          business.
        </h4>
        <p>
          <strong>Start</strong> April 17th 2023 <br/>
          <strong>Duration</strong> 12 weeks (+4 weeks online preparation) <br/>
          <strong>Times</strong> 5 days/week, 9am - 6pm <br/>
          <strong>Price</strong> $13,999 (payment plans available) <br/>
          <strong>Program</strong> Fullstack (Frontend & Backend) <br/>
          <strong>Technologies</strong>
          HTML, CSS, JavaScript, React, Node.js, Next.js, GraphQL, PostgreSQL, GitHub and many more <br/>
          <strong>Experience</strong> no upfront coding knowledge needed <br/>
        </p>
        <h4>
          Do you have questions? <br/>
          Let's talk! Click the link below to schedule time with us.
        </h4>

        <Modal>
          <template #trigger="{ toggleOpen }">
            <CoreButton size="L" variant="secondary" @click="toggleOpen()">
              Schedule A Meeting
            </CoreButton>
          </template>

          <template #content>
            <div
                :style="{ flex: 1 }"
                class="calendly-inline-widget"
                data-url="https://calendly.com/the-earth-is-square/30min"
            />
          </template>
        </Modal>
      </div>

      <div class="course-information__images">
        <div class="course-information__image --1"/>
        <div class="course-information__image --2"/>
        <div class="course-information__image --3"/>
        <div class="course-information__image --4"/>
        <div class="course-information__image --5"/>
        <div class="course-information__image --6"/>
      </div>
    </div>
  </section>
</template>

<script lang="ts" setup>
onMounted(() => {
  const recaptchaScript = document.createElement('script')
  recaptchaScript.setAttribute('src', 'https://assets.calendly.com/assets/external/widget.js')
  document.head.appendChild(recaptchaScript)
})
</script>

<style lang="scss" scoped>
#course-information {
  display: flex;
  justify-content: center;
  height: 60vh;
  padding: 5rem 5%;
  border-radius: var(--BorderRadius-L);
  background-color: var(--Color-White);

  .course-information__content {
    position: relative;
    display: grid;
    align-items: center;
    flex: 1;
    max-width: var(--View-MaxWidth);
    background-color: var(--Color-White);
    grid-template-columns: 1fr 1fr;

    .course-information-content__left {
      font-size: var(--FontSize-M);
      display: flex;
      flex-direction: column;
      gap: 5rem;

      h1 {
        font-size: var(--FontSize-Chonky-L);
        line-height: 72.19%;
        color: var(--Color-White);
        text-shadow: var(--Shadow-Border), var(--Shadow-L);
      }

      button {
        margin-right: auto;
      }
    }

    .course-information__images {
      position: relative;
      height: 100%;

      .course-information__image {
        position: absolute;
        background-size: cover;
        border-radius: var(--BorderRadius-L);
        box-shadow: var(--Shadow-L);

        &.--1 {
          background-image: url("@/assets/img/upleveled_15.avif");
          width: 8vw;
          height: 8vw;
          top: 0;
          left: 6vw;
        }

        &.--2 {
          background-image: url("@/assets/img/upleveled_6.avif");
          width: 12vw;
          height: 12vw;
          top: 10vw;
          left: 9vw;
        }

        &.--3 {
          background-image: url("@/assets/img/upleveled_16.avif");
          width: 14vw;
          height: 14vw;
          top: 4vw;
          left: 23vw;
        }

        &.--4 {
          background-image: url("@/assets/img/upleveled_11.avif");
          width: 7vw;
          height: 7vw;
          top: 16vw;
          left: 0;
        }

        &.--5 {
          background-image: url("@/assets/img/upleveled_1.avif");
          width: 8vw;
          height: 8vw;
          top: 24vw;
          left: 11vw;
        }

        &.--6 {
          background-image: url("@/assets/img/upleveled_5.avif");
          width: 10vw;
          height: 10vw;
          top: 25vw;
          left: 22vw;
        }
      }
    }
  }
}
</style>