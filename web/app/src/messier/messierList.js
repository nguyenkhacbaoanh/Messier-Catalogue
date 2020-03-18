import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import IconButton from '@material-ui/core/IconButton';
import StarBorderIcon from '@material-ui/icons/StarBorder';

import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
    backgroundColor: theme.palette.background.paper,
  },
  gridList: {
    flexWrap: 'nowrap',
    // Promote the list into his own layer on Chrome. This cost memory but helps keeping high FPS.
    transform: 'translateZ(0)',
  },
  title: {
    color: theme.palette.primary.light,
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  titleBar: {
    background:
      'linear-gradient(to top, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 70%, rgba(0,0,0,0) 100%)',
  },
}));

/**
 * The example data is structured as follows:
 *
 * import image from 'path/to/image.jpg';
 * [etc...]
 *
 * const tileData = [
 *   {
 *     img: image,
 *     title: 'Image',
 *     author: 'author',
 *   },
 *   {
 *     [etc...]
 *   },
 * ];
 */

const tileData = {
    data : [
    {
      id: "M23",
      designations: [
      {
      other_name: "messier 23"
      },
      {
      other_name: " m23"
      },
      {
      other_name: " ngc 6494"
      },
      {
      other_name: " collinder 356"
      },
      {
      other_name: " c 1753-190"
      },
      {
      other_name: " mwsc 2757"
      }
      ],
      messier_type: "open",
      messier_object: "cluster",
      constellation: "sagittarius",
      right_ascension: "17h 56.8m",
      declination: "-19°01′",
      distance: "2,150 light years (659 parsecs)",
      apparent_magnitude: "+6.9",
      apparent_dimensions: "27′",
      radius: "8 light years",
      age: "220 million years",
      year: "1764.0",
      number_of_stars: "176",
      discoverer: "Messier",
      image: [
      {
      image_url: "https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-23.jpg",
      image_description: "Messier 23. Image: Wikisky"
      },
      {
      image_url: "https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-23-Messier-21-Trifid-and-Omega.jpg",
      image_description: "Messier 23, Messier 21, Trifid Nebula (M20) and Omega Nebula (M17). Image: Wikisky"
      },
      {
      image_url: "https://www.messier-objects.com/wp-content/uploads/2015/04/M23.jpg",
      image_description: "Messier 23. Atlas Image mosaic obtained as part of the Two Micron All Sky Survey (2MASS), a joint project of the University of Massachusetts and the Infrared Processing and Analysis Center/California Institute of Technology, funded by the National Aeronautics and Space Administration and the National Science Foundation."
      },
      {
      image_url: "https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-23-location.png",
      image_description: "Messier 23 location. Image: IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg)"
      }
      ],
      video: [ ]
    },
    {
      id: "M1",
      designations: [
        {
        other_name: "messier 1"
        },
        {
        other_name: " m1"
        },
        {
        other_name: " crab nebula"
        },
        {
        other_name: " ngc 1952"
        },
        {
        other_name: " sharpless 244"
        },
        {
        other_name: " lbn 833"
        },
        {
        other_name: " 3c 144"
        }
      ],
      messier_type: "supernova remnant",
      messier_object: "nebula",
      features: "optical pulsar",
      constellation: "taurus",
      right_ascension: "05h 34m 31.94s",
      declination: "+22°00’52.2”",
      distance: "6,500 light years (2 kiloparsecs)",
      apparent_magnitude: "+8.4",
      absolute_magnitude: "-3.1",
      apparent_dimensions: "420″ × 290” (6×4 arc minutes)",
      radius: "5.5 light years (1.7 parsecs)",
      year: "1731.0",
      discoverer: "Bévis",
      image: [
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Messier-1.jpg",
        image_description: "Messier 1 – The Crab Nebula. This is a mosaic image, one of the largest ever taken by NASA’s Hubble Space Telescope of the Crab Nebula, a six-light-year-wide expanding remnant of a star’s supernova explosion. Japanese and Chinese astronomers recorded this violent event nearly 1,000 years ago in 1054, as did, almost certainly, Native Americans. The orange filaments are the tattered remains of the star and consist mostly of hydrogen. The rapidly spinning neutron star embedded in the center of the nebula is the dynamo powering the nebula’s eerie interior bluish glow. The blue light comes from electrons whirling at nearly the speed of light around magnetic field lines from the neutron star. The neutron star, like a lighthouse, ejects twin beams of radiation that appear to pulse 30 times a second due to the neutron star’s rotation. A neutron star is the crushed ultra-dense core of the exploded star. Image: NASA, ESA, J. Hester and A. Loll (Arizona State University)"
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Crab-Nebula-Hubble.jpg",
        image_description: "Hubble Space Telescope image of filaments in the Crab Nebula (M1, NGC 1952). Credit: NASA and The Hubble Heritage Team (STScI/AURA)"
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Crab-Nebula-Lord-Rosse.jpg",
        image_description: "Drawing of the Crab Nebula. Originally published in Observations on Some of the Nebulae, Philosophical Transactions of the Royal Society of London vol. 134 (1844). Image: William Parsons, 3rd Earl of Rosse"
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Messier-1-location.png",
        image_description: "Location of the Crab Nebula (Messier 1) in Taurus constellation. Image: IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg)"
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Crab-Pulsar.gif",
        image_description: "What if you could “see” in gamma-rays? If you could, these two spinning neutron stars or pulsars would be among the brightest objects in the sky. This computer processed image shows the Crab Nebula pulsar (below and right of center) and the Geminga pulsar (above and left of center) in the “light” of gamma-rays. Gamma-ray photons are more than 10,000 times more energetic than visible light photons and are blocked from the Earths’s surface by the atmosphere. This image was produced by the high energy gamma-ray telescope “EGRET” on board NASA’s orbiting Compton Observatory satellite. Image: NASA, Compton Gamma Ray Observatory."
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Messier-1-Hubble.jpg",
        image_description: "This image shows a composite view of the Crab Nebula as viewed by the Herschel Space Observatory and the Hubble Space Telescope. The image combines Hubble’s view of the nebula at visible wavelengths, obtained using three different filters sensitive to the emission from oxygen and sulphur ions and is shown here in blue. Herschel’s far-infrared image reveals the emission from dust in the nebula and is shown here in red. While studying the dust content of the Crab Nebula with Herschel, a team of astronomers have detected emission lines from argon hydride, a molecular ion containing the noble gas argon. This is the first detection of a noble-gas based compound in space. Image: ESA/Herschel/PACS/MESS Key Programme Supernova Remnant Team; NASA, ESA and Allison Loll/Jeff Hester (Arizona State University)"
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/M1.png",
        image_description: "This is the Crab Nebula in various energy bands, including a hard X-ray image from the HEFT data taken during its 2005 observation run. The angular resolution of HEFT is about 1.5′. Each image is 6′ wide. Image: NASA, CM Hubert Chen, Fiona A. Harrison, Principal Investigator, Caltech Charles J. Hailey, Columbia Principal, Columbia, Finn E. Christensen, DSRI Principal, DSRI, William W. Craig, Optics Scientist, LLNL, Stephen M. Schindler, Project Manager, Caltech"
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Messier-1-NASA.jpg",
        image_description: "Crab Nebula in visible light taken by the Hale Observatory optical telescope in 1959. Credit: NASA Marshall Space Flight Center (NASA-MSFC)"
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Messier-1-false-colour.jpg",
        image_description: "The Crab Nebula (Messier 1) is a well-known supernova remnant (the remains from massive star whose life ended in a massive explosion). This false-color image of the Crab Nebula was taken at the Vatican Observatory on Mount Graham using Sloan u’, g’, and r’ filters. The yellow filaments on the outside of the remnant are primarily ionized hydrogen gas and show up in both the u’ and r’ filters. The gas in the interior of the nebula is heated by the neutron star left by the explosion and its glowing light is visible in all the filters. While the neutron star itself is too faint to be see in the visible, the glowing disk of gas and debris that surround it also shows up quite clearly in the g’ filter (blue-white colors). One of the jets thrown off by the accreting neutron star is also partially visible in the g’ filter to the lower-left of the accretion disk. Image: Jjstott at wikipedia.org"
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Messier-1-Chandra.jpg",
        image_description: "In the Crab Nebula, a rapidly rotating neutron star, or pulsar (white dot near the center), powers the dramatic activity seen by Chandra. The inner X-ray ring is thought to be a shock wave that marks the boundary between the surrounding nebula and the flow of matter and antimatter particles from the pulsar. Energetic particles move outward to brighten the outer ring and produce an extended X-ray glow. The jets perpendicular to the ring are due to matter and antimatter particles spewing out from the poles of the pulsar. The fingers, loops and bays visible on the outer boundary of the nebula are likely caused by confinement of the high-energy particles by magnetic forces. Image: Chandra X-ray Observatory, Smithsonian Institution, NASA/CXC/SAO/F.Seward et al."
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Crab-Nebula-supernova-remnant.jpg",
        image_description: "This view of the supernova remnant obtained by the Spitzer Space Telescope shows the infrared view of this complex object. The blue-white region traces the cloud of energetic electrons trapped within the star’s magnetic field, emitting so-called “synchrotron” radiation. The red features follow the well-known filamentary structures that permeate this nebula. Though they are known to contain hot gasses, their exact nature is still a mystery that astronomers are examining. The energetic cloud of electrons are driven by a rapidly rotating neutron star, or pulsar, at its core. The nebula is about 6,500 light-years away from the Earth, and is 5 light-years across. This false-color image presents images from Spitzer’s Infrared Array Camera (IRAC) at 3.6 (blue), 4.5 (green), and 8.0 (red) microns. Image: NASA/JPL-Caltech/R. Gehrz (University of Minnesota)"
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Crab-Pulsar-Hubble.jpg",
        image_description: "Hubble Space Telescope observations of features very close to the Crab Pulsar, changing over time. Image: NASA"
        },
        {
        image_url: "https://www.messier-objects.com/wp-content/uploads/2015/01/Messier-1-composite.jpg",
        image_description: "A composite image of the Crab Nebula showing the X-ray (blue), and optical (red) images superimposed. The size of the X-ray image is smaller because the higher energy X-ray emitting electrons radiate away their energy more quickly than the lower energy optically emitting electrons as they move. Optical: NASA/HST/ASU/J. Hester et al. X-Ray: NASA/CXC/ASU/J. Hester et al."
        }
      ],
      video: [
        {
        video_url: "www.youtube.com/embed/vPxLVgTIAbk?rel=0"
        },
        {
        video_url: "www.youtube.com/embed/qDhdwgK218E?rel=0"
        },
        {
        video_url: "www.youtube.com/embed/Qyc4bgK7AXE?rel=0"
        }
      ]
    },
  ]
}

// const m = tileData.data[0].image

// const dt = tileData.data

export default function SingleLineGridList(props) {
  // const data = this.props;
  const classes = useStyles();

  return (
    <React.Fragment>
    <div className={classes.content}>
      <CssBaseline />
      <Container fixed>
        {props.data.map(m => {
          return (
            <div>
              <div>{m.id}</div>
              <GridList className={classes.gridList} cols={4}>
                {m.image.map(i => (
                  <GridListTile key={i.id}>
                    <img src={i.image_url} alt={i.image_url} />
                    <GridListTileBar
                      title={m.id}
                      classes={{
                        root: classes.titleBar,
                        title: classes.title,
                      }}
                      actionIcon={
                        <IconButton aria-label={`star ${i.id}`}>
                          <StarBorderIcon className={classes.title} />
                        </IconButton>
                      }
                    />
                  </GridListTile>
                ))}
              </GridList>
            </div>
          )
        }
        )}
      </Container>
      </div>
    </React.Fragment>)
    // <div className={classes.root}>
      // <GridList className={classes.gridList} cols={2.5}>
      //   {m.map(i => (
      //     <GridListTile key={i.image_url}>
      //       <img src={i.image_url} alt={i.image_url} />
      //       <GridListTileBar
      //         title={i.image_url}
      //         classes={{
      //           root: classes.titleBar,
      //           title: classes.title,
      //         }}
      //         actionIcon={
      //           <IconButton aria-label={`star ${i.image_url}`}>
      //             <StarBorderIcon className={classes.title} />
      //           </IconButton>
      //         }
      //       />
      //     </GridListTile>
      //   ))}
      // </GridList>
        {/* {props.data.map(tile => (
          <GridListTile key={tile.id}>
            {tile.image &&
            <img src={tile.image[0].image_url} alt={tile.id} />
            }
            <GridListTileBar
              title={tile.id}
              classes={{
                root: classes.titleBar,
                title: classes.title,
              }}
              actionIcon={
                <IconButton aria-label={`star ${tile.id}`}>
                  <StarBorderIcon className={classes.title} />
                </IconButton>
              }
            />
          </GridListTile>
        ))} */}
      {/* </GridList> */}
    {/* </div> */}
  // );
}
