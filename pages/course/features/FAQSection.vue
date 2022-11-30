<template>
  <section id="faq">
    <div class="faq__inner-wrapper">
      <div class="faq__header">
        <div class="faq__header-background" />
        <h2>FAQ</h2>
      </div>
      <div class="faq__questions">
        <div class="faq__questions-background" />

        <div v-for="question in questions" :key="question.question" class="faq__question">
          <span>{{ question.question }}</span> {{ question.answer }}
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts" setup>
const questions = [
  {
    question: "Why bootcamps?",
    answer:
        `The educational model of bootcamps is already widely established in other countries because
        participants and employers love the focus on the development of practical skills and the use of industry
        best-practices. Plus: the condensed format puts you in the game fast – with excellent skills and without
        having to cover long periods without salary.`
  },
  {
    question: "In-person or remote?",
    answer:
        `Following all relevant Covid hygiene regulations we always try to provide as much of an in-person experience
        as possible. Independent from safety considerations you are always free to join remotely.`
  },
  {
    question: "Do I need upfront knowledge?",
    answer:
        `Our curriculum is designed to take you from “no experience at all” to “I’m a developer”. All you need is
        to understand that coding comes with life-long-learning – even for the experts, and to be honest: That’s
        half the fun.`
  },
];
</script>

<style lang="scss" scoped>
#faq {
  .faq__inner-wrapper {
    display: flex;
    max-width: 144rem;
    margin: 0 auto;
    gap: 0.6rem;

    .faq__header {
      position: relative;
      margin-top: auto;
      padding: 1rem;
      color: var(--white);
      text-orientation: upright;
      writing-mode: vertical-rl;

      h2 {
        font-size: 5.4rem;
        font-weight: 900;
        line-height: 4rem;
        position: relative;
        padding-right: 5rem;
      }

      .faq__header-background {
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        // left: calc(0px - (((100vw - (view-border(x2) + scrollbar-width(?) + padding)) - max-width) / 2));
        left: calc(0px - (((100vw - (1.2rem + 1.1rem + 1rem)) - 144rem) / 2));
        border-radius: 3rem;
        background: linear-gradient(247.29deg, #EB2188 7.21%, #D909DD 91.17%);
      }
    }

    .faq__questions {
      position: relative;
      display: flex;
      flex-direction: column;
      padding: 3rem 0 3rem 3rem;
      gap: 3rem;

      .faq__question {
        font-size: 1.728rem;
        font-weight: 700;
        position: relative;

        span {
          font-size: 3.583rem;
          font-weight: 900;
          background: linear-gradient(247.29deg, #EB2188 7.21%, #D909DD 91.17%);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }
      }

      .faq__questions-background {
        position: absolute;
        top: 0;
        // right: calc(0px - (((100vw - (view-border(x2) + scrollbar-width(?) + padding)) - max-width) / 2));
        right: calc(0px - (((100vw - (1.2rem + 1.1rem + 1rem)) - 144rem) / 2));
        bottom: 0;
        left: 0;
        border-radius: 3rem;
        background-color: var(--white);
      }
    }
  }
}
</style>