<template>
  <div class="powers">
    <h3>Are You Ready To<br />Gain These Powers?</h3>
    <div class="powers__icons">
      <img :style="{ left: '40%', top: 0, width: '5vw' }" alt="css" src="@/assets/img/css.png" />
      <img :style="{ right: '10%', top: '80%', width: '5vw' }" alt="docker" src="@/assets/img/docker.png" />
      <img :style="{ left: '5%', top: '50%', width: '5vw' }" alt="github" src="@/assets/img/github.png" />
      <img :style="{ left: '15%', top: '76%', width: '4vw' }" alt="next-js" src="@/assets/img/next-js.png" />
      <img :style="{ left: '35%', top: '25%', width: '6vw' }" alt="javascript" src="@/assets/img/javascript.png" />
      <img :style="{ left: '35%', top: '60%', width: '5vw' }" alt="graphql" src="@/assets/img/graphql.png" />
      <img :style="{ right: 0, width: '5vw' }" alt="html" src="@/assets/img/html.png" />
      <img :style="{ right: '10%', top: '30%', width: '4vw' }" alt="node-js" src="@/assets/img/node-js.png" />
      <img :style="{ right: '10%', top: '50%', width: '6vw' }" alt="react-js" src="@/assets/img/react-js.png" />
      <img :style="{ left: '5%', top: '15%', width: '5vw' }" alt="typescript" src="@/assets/img/typescript.png" />
    </div>

    <div class="powers__cta">
      <router-link to="course">
        <CoreButton variant="secondary">
          ...And More!
        </CoreButton>
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.powers {
  display: flex;
  overflow: hidden;
  flex-direction: column;
  border-radius: 3rem;
  grid-column: span 4;
  grid-row: span 10;

  h3 {
    font-size: 2.4rem;
    margin: 5% 0 0 5%;
    transform: rotate(-7deg);
    color: var(--white);
  }

  .powers__icons {
    position: relative;
    flex: 1;

    img {
      position: absolute;
      transition: all 0.25s ease;

      &:hover {
        transform: scale(1.1, 1.1);
      }
    }
  }

  .powers__cta {
    display: flex;
    justify-content: center;
  }
}
</style>