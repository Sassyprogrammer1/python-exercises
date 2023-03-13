// if (body.rankings && body.locations && body.employments) {
//     // create query for locations
//     const locations = body.locations;
//     const rankings = body.rankings;
//     const employments = body.employments;

//     console.log(employments);
//     // Locations search query
//     const locationsSearchQuery = {
//       _source: ['_id', 'comments', '_parent', 'name', 'geotag'],
//       query: {
//         terms: {
//           geotag: locations,
//         },
//       },
//     };
//     //Employments Seach Query
//     const employmentsSearchQuery = {
//       _source: ['name'],
//       query: {
//         nested: {
//           path: 'courses.minor',
//           query: {
//             terms: {
//               'courses.minor.courseName': employments,
//             },
//           },
//         },
//       },
//     };

//     try {
//       // call the locations query
//       let search = await client.search({
//         index: 'universities',
//         body: locationsSearchQuery,
//       });
//       // resolve the promise
//       let resolvedPromise = await Promise.all([search]);
//       // map through the results of the locations query and return an
//       // array of universities names which are present in the rankings payload
//       console.log(resolvedPromise[0].body.hits.hits);
//       const filteredLocationNames =
//         resolvedPromise[0].body.hits.hits.map((result: any) => {
//           if (rankings.includes(result._source.name)) {
//             return result._source.name;
//           }
//         });
//       // eliminate the undefined values
//       var filtered = filteredLocationNames.filter(
//         (x: any) => x !== undefined,
//       );
//       //console.log('Filtered Locations', filtered);

//       // call the employments query
//       let searchTwo = await client.search({
//         index: 'universities',
//         body: employmentsSearchQuery,
//       });
//       //resolve the promise
//       let resolvedPromiseTwo = await Promise.all([searchTwo]);
//       //map through the results of the employments query and return an
//       //array of universities names which are present in "filteredLocationNames"
//       const filteredEmployments =
//         resolvedPromiseTwo[0].body.hits.hits.map((result: any) => {
//           if (filtered.includes(result._source.name)) {
//             return result._source.name;
//           }
//         });
//       console.log(filteredEmployments);
//       // remove the undefined values
//       var filteredTwo = filteredEmployments.filter(
//         (x: any) => x !== undefined,
//       );
//       return filteredTwo;
//     } catch (err) {
//       console.log(err);
//       return setResponse(err.statusCode, {
//         message: err.message,
//       });
//     }
//   } else if (body.rankings && body.locations && !body.employments) {
//     // Write Code Here

//     const rankings = body.rankings;
//     const locations = body.locations;

    
//     // call query with Geotag and eliminate the unis from the rankings that are

//     const locationsSearchQuery = {
//       _source: ['_id', 'comments', '_parent', 'name', 'geotag'],
//       query: {
//         terms: {
//           geotag: locations,
//         },
//       },
//     };

//     try {
//       let search = await client.search({
//         index: 'universities',
//         body: locationsSearchQuery,
//       });

//       // resolve the promise
//       let resolvedPromise = await Promise.all([search]);

//       // map through the results of the locations query
//       // return an array of universities names which are present in the rankings payload

//       const filteredLocationNames = resolvedPromise[0].body.hits.hits.map((result:any) => {
//         if(rankings.includes(result._source.name)){
//           return result._source.name
//         }
//       });

//       // eliminate the undefined values

//       var filtered = filteredLocationNames.filter((x:any) => x !== undefined,);
//       return filtered
//     } catch (err){
//       console.log(err);
//       return setResponse(err.statusCode, {
//         message: err.message,
//       });
//     }
//     // present in the rankings but not in the Locations
//   } else if (body.rankings && body.employments && !body.locations) {
//     // Write Code Here
    
//     const rankings = body.rankings;
//     const employments = body.employments

//     // Employments Search Query
//     const employmentsSearchQuery = {
//       _source: ['name'],
//       query: {
//         nested: {
//           path: 'courses.minor',
//           query: {
//             terms: {
//               'courses.minor.courseName': employments,
//             },
//           },
//         },
//       },
//     };

//     try{
//       let search = await client.search({
//         index: 'universities',
//         body: employmentsSearchQuery
//       })

//       //resolve the promise
//       let resolvedPromise = await Promise.all([search])

//       //map through the results of them employments query

//       //return an array of array of universities name
//       const filteredEmployments = resolvedPromise[0].body.hits.hits.map((result:any) => {
//         if(rankings.includes(result._source.name)){
//           return result._source.name
//         }
//       });

//       var filtered = filteredEmployments.filter((x: any) => x !== undefined,);
//       return filtered
//     }catch (err) {
//       console.log(err);
//       return setResponse(err.statusCode, {
//       message: err.messge,
//       });
//       }

//     // call query with coursename for employments and eliminate the unis from the rankings that are
//     // present in the rankings but not in the employments
//   } else if (body.rankings && !body.locations && !body.employments) {
    
//     // Write Code Here
//     const rankings = body.rankings;
    
//     // const rankingsSearchQuery;
//     const normalizedRankings = rankings.map((name:any) => name.toLowerCase().replace(/^the?\s*(\S+)\s.*?(\b(?:university|college)\b)?$/g, '$1$2').trim());
//     // const normalizedRankings = rankings.map(name => name.toLowerCase().replace(/^(the\s+)?(.+?)\s+(university|college)$/g, '$2').trim());

//     console.log(normalizedRankings)
  
//     const rankingssearchQuery = {
//       _source: ['name'],
//       query: {
//         terms: {
//          name : normalizedRankings
//         }
//       }
//     }
    
//     try {
//       let search = await client.search({
//         index: 'universities',
//         body: rankingssearchQuery
//       })

//       // resolve the promise
//       let resolvedPromise = await Promise.all([search])

//       console.log(resolvedPromise)

//       const filteredRankings = resolvedPromise[0].body.hits.hits.map((result: any) => {
//         // if(rankings.includes(result._source.name)){
//           return result._source.name
//         // }
//       });

//       console.log(filteredRankings)

//       var filtered2  = filteredRankings.filter((x: any) => x !== undefined,);
//       return filtered2
//     } catch (err){
//       console.log(err);
//       return setResponse(err.statusCode,{
//         message: err.message,
//       });
//     }
   

//     // return only the rankings array of uni names
//   } else if (body.locations && !body.employments && !body.rankings) {
//     // Write Code Here

//     const locations = body.locations;
    
//     // call the query with geoTag and return an array of the uniNames return by the

//     const locationsSearchQuery = {
//       _source: ['_id', 'comments', '_parent', 'name', 'geotag'],
//       query: {
//         terms: {
//           geotag: locations,
//         },
//       },
//     };

//     try {
//       let search  = await client.search({
//         index: 'universities',
//         body: locationsSearchQuery,
//       });

//       let resolvedPromise = await Promise.all([search]);

//       const filteredLocationNames = 
//       resolvedPromise[0].body.hits.hits.map((result: any) => {
//       return result._source.name;
      
//       });

//       var filtered = filteredLocationNames.filter((x: any) => x !== undefined,);

//       return filtered

//     } catch (err){
//       console.log(err);
//       return setResponse(err.statusCode, {
//         message: err.message,
//       })
//     }

//     // query containing the locations mentioned
//   } else if (body.employments && !body.locations && !body.rankings) {
//     //Write Code Here
//     const employments = body.employments

    
//     // call the query with employemts cournames and return the array with the uni names

//     const employmentsSearchQuery = {
//       _source: ['name'],
//       query: {
//         nested: {
//           path: 'courses.minor',
//           query: {
//             terms: {
//               'courses.minor.courseName': employments,
//             },
//           },
//         },
//       },
//     };
//     try {
//     let search = await client.search({
//       index: 'universities',
//       body: employmentsSearchQuery
//     });

//     let resolvedPromiseTwo = await Promise.all([search])

//     const filteredEmployments = resolvedPromiseTwo[0].body.hits.hits.map((result: any) => {
//       return result._source.name
//     })

//     var filtered = filteredEmployments.filter((x: any) => x!== undefined,);
//     return filtered
//   } catch (err){
//     console.log(err);
//     return setResponse(err.statusCode, {
//       message:err.message,
//     });
//   }
//   } else if (body.employments && body.locations && !body.rankings) {
//     // Write Code here
//     const employments = body.employment;
//     const locations = body.locations
//     // in this condition we will call the query with the multiple field names
    
    
    
//     const searchQuery = {
//       _source: ['name'],
//       query: {
//         terms:{
//           geotag: locations,
//           'courses.minor.courseName': employments,
//         }
//       }
//     }
    
//     try{
//       let search = await client.search({
//         index: 'universities',
//         body: searchQuery,
//       })

//       let resolvedPromise = await Promise.all([search]);

//       const filteredQuery = resolvedPromise[0].body.hits.hits.map((result: any) => {
//         return result._source.name
//       })
//       return filteredQuery
//     }catch(err){
//       console.log(err);
//       return setResponse(err.statusCode,{
//       message: err.message,
//       });
//       }
     
    
//     // call the query with employments and locations
   

//     // and return the array of uni names
//   }