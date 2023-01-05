<template>
  <section id="outcomes">
    <div class="outcomes__inner-wrapper">
      <div class="outcomes__header">
        Launch Your <span>Career</span>
      </div>

      <div class="outcomes__panels">
        <div v-for="panel in panels" class="outcomes__panel">
          <div class="outcomes__panel-icon">
            <Icon :name="panel.icon" size="6rem" />
          </div>

          <div class="outcomes__panel-title">
            {{ panel.title }}
          </div>

          <div class="outcomes__panel-description">
            {{ panel.description }}
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts" setup>
const panels = [
  {
    title: "Mentorship",
    description: "We will guide you from day 1 of your journey and focus on your personal strengths and goals.",
    icon: "rocket"
  },
  {
    title: "Planning",
    description: "You will finish the course with a full set of strong online & offline profiles, interview prep, tips & tricks for the application process.",
    icon: "rocket"
  },
  {
    title: "Graduation Event",
    description: "The presentation of your final project will be viewed by employers from all over who will invite you to job interviews.",
    icon: "rocket"
  },
  {
    title: "Networking",
    description: "You profile incl. projects and contacts will be featured on our online matching platform “Fusion” to make it easily accessible to employers ",
    icon: "rocket"
  },
  {
    title: "On The Job Mentoring",
    description: "Would you like ongoing support during the first months of your job or when launching as a freelancer? We get you unstuck with our Mentoring subscription",
    icon: "rocket"
  },
  {
    title: "Matching on Fusion",
    description: "You profile incl. projects and contacts will be featured on our online matching platform “Fusion” to make it easily accessible to employers ",
    icon: "rocket"
  }
];
</script>

<style lang="scss" scoped>
#outcomes {
  display: flex;
  justify-content: center;
  padding: 10rem 0;

  .outcomes__inner-wrapper {
    font-weight: var(--FontWeight-Bold);
    display: flex;
    flex-direction: column;
    max-width: var(--View-MaxWidth);
    gap: 5rem;

    .outcomes__header {
      font-size: 6.484rem;
      text-align: center;
      color: var(--Color-White);

      span {
        background: var(--Gradient-PinkPurple);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        border-bottom: 0.3rem solid var(--Color-Pink);
      }
    }

    .outcomes__panels {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-gap: 5rem 6rem;

      .outcomes__panel {
        position: relative;
        display: flex;
        flex-direction: column;
        padding: 5rem 0 0 5rem;

        .outcomes__panel-icon {
          position: absolute;
          top: 0;
          left: 0;
          fill: url('#teis_gradient');
        }

        .outcomes__panel-title {
          font-weight: var(--FontWeight-Black);
          font-size: var(--FontSize-XXL);
          background: var(--Gradient-PinkPurple);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
        }

        .outcomes__panel-description {
          font-size: var(--FontSize-M);
          color: white;
        }
      }
    }
  }
}
</style>