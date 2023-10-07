using System;
using UnityEngine;
using UnityEngine.Perception.Randomization.Randomizers;

namespace SynthDet.RandomizerTags
{
    [AddComponentMenu("SynthDet/RandomizerTags/CameraPositionRandomizerTag")]
    [RequireComponent(typeof(Camera))]
    public class CameraPositionRandomizerTag : RandomizerTag { }
}

