using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
//using WebApiTest2.Models;

namespace WebApiTest2.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class DriftingObjectsController : ControllerBase
    {

        private static readonly string[] Names = new[]
            {
                "Container", "Dead body", "Whale", "Lumber", "Giant fish net", "Boat", "Large boat", "Whirlpool"
        };

        public DriftingObjectsController()
        {
        }
        // GET: api/DriftingObjects
        [HttpGet("")]
        public ActionResult<IEnumerable<DriftingObject>> GetDriftingObjects()
        {

            return Enumerable.Range(1, 5).Select(index => new DriftingObject
            {
                name = Names[Random.Shared.Next(Names.Length)],
                latitude = 63.4601944,
                longitude = 10.35175
                
            })
            .ToArray();
        }
        // GET: api/DriftingObjects/3
        [HttpGet("{id}")]
        public ActionResult<DriftingObject> GetDriftingObjectById(int id)
        {
            return null;
        }
        // POST: api/DriftingObjects
        [HttpPost("")]
        public ActionResult<DriftingObject> PostDriftingObject(DriftingObject model)
        {
            return null;
        }
        // POST: api/DriftingObjects/4
        [HttpPut("{id}")]
        public IActionResult PutDriftingObject(int id, DriftingObject model)
        {
            return NoContent();
        }
        // DELETE: api/DriftingObjects/6
        [HttpDelete("{id}")]
        public ActionResult<DriftingObject> DeleteDriftingObjectById(int id)
        {
            return null;
        }
    }
    
}