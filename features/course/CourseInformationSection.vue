<template>
  <section id="course-information">
    <div class="course-information__content">
      <div class="course-information-content__left">
        <Heading font="PassionOne" type="h1">
          WEB DEVELOPMENT<br/>BOOTCAMP
        </Heading>

        <strong>
          Ready for a change? Become a professional Web Developer and boost your career or launch your own
          business.
        </strong>

        <p>
          <strong>Start</strong>
          April 17th 2023 <br/>

          <strong>Duration</strong>
          12 weeks (+4 weeks online preparation) <br/>

          <strong>Times</strong>
          5 days/week, 9am - 6pm <br/>

          <strong>Price</strong>
          <s>$13,999</s> <strong>$6,999 - 50% Grand Opening Special!</strong> <i>(payment plans available)</i> <br/>

          <strong>Program</strong>
          Fullstack (Frontend & Backend) <br/>

          <strong>Technologies</strong>
          HTML, CSS, JavaScript, React, Node.js, Next.js, GraphQL, PostgreSQL, GitHub and many more <br/>

          <strong>Experience</strong>
          no upfront coding knowledge needed <br/>
        </p>

        <strong>
          Do you have questions? <br/>
          Let's talk! Click the link below to schedule time with us.
        </strong>

        <Modal v-if="isDesktop">
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

        <NuxtLink target="_blank" to="https://calendly.com/the-earth-is-square/30min">
          <CoreButton size="L" variant="secondary">
            Schedule A Meeting
          </CoreButton>
        </NuxtLink>
      </div>

      <div v-if="isDesktop" class="course-information__images">
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
import { useScreen } from "~/hooks/useScreen";

const { isDesktop } = useScreen()

onMounted(() => {
  const recaptchaScript = document.createElement('script')
  recaptchaScript.setAttribute('src', 'https://assets.calendly.com/assets/external/widget.js')
  document.head.appendChild(recaptchaScript)
})
</script>

<style lang="scss" scoped>
@import 'assets/style/variables.scss';

#course-information {
  display: flex;
  justify-content: center;
  height: 60vh;
  padding: 5rem 5%;
  border-radius: var(--BorderRadius-L);
  background-color: var(--Color-White);
  overflow: hidden;

  @media screen and (max-width: $BreakPoint-Tablet) {
    padding: 0;
    text-align: center;
    height: auto;
  }

  .course-information__content {
    position: relative;
    display: grid;
    align-items: center;
    flex: 1;
    max-width: var(--View-MaxWidth);
    background-color: var(--Color-White);
    grid-template-columns: 1fr 1fr;

    @media screen and (max-width: $BreakPoint-Tablet) {
      transform: scale(0.9, 0.9);
      grid-template-columns: 1fr;
    }

    .course-information-content__left {
      font-size: var(--FontSize-M);
      display: flex;
      flex-direction: column;
      gap: 5rem;

      @media screen and (max-width: $BreakPoint-Tablet) {
        gap: 2rem;
      }

      s {
        margin-left: 0.5rem;
      }

      button {
        margin-right: auto;

        @media screen and (max-width: $BreakPoint-Tablet) {
          margin: auto;
        }
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
          background-image: url("assets/img/upleveled_15.avif");
          width: 8vw;
          height: 8vw;
          top: 0;
          left: 6vw;
        }

        &.--2 {
          background-image: url("assets/img/upleveled_6.avif");
          width: 12vw;
          height: 12vw;
          top: 10vw;
          left: 9vw;
        }

        &.--3 {
          background-image: url("assets/img/upleveled_16.avif");
          width: 14vw;
          height: 14vw;
          top: 4vw;
          left: 23vw;
        }

        &.--4 {
          background-image: url("assets/img/upleveled_11.avif");
          width: 7vw;
          height: 7vw;
          top: 16vw;
          left: 0;
        }

        &.--5 {
          background-image: url("assets/img/upleveled_1.avif");
          width: 8vw;
          height: 8vw;
          top: 24vw;
          left: 11vw;
        }

        &.--6 {
          background-image: url("assets/img/upleveled_5.avif");
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