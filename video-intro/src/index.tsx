import { Composition, registerRoot } from "remotion";
import { MainVideo } from "./MainVideo";

registerRoot(() => (
  <Composition
    id="MainVideo"
    component={MainVideo}
    durationInFrames={600}
    fps={30}
    width={1920}
    height={1080}
  />
));
